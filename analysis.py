import pandas as pd
import matplotlib.pyplot as plt

#################################################################################
# Helper Functions 
#################################################################################

def sparql_to_df(g, q):
    """
    Transforms sparql query result into a pandas dataframe called metadata, and uses this to retrieve timeseries data
    Input: rdf graph g and sparql query q
    Output: metadata and timeseries pandas dataframes
    """

    # query the graph 
    res = g.query(q)

    # convert to SparqlResult to a pandas dataframe with column names relfecting variables in sparql query 
    md = pd.DataFrame.from_records(data=list(res),columns=res.vars)
    md = md.applymap(str) #convert everything to a string 
    md.columns = [x.strip() for x in md.columns]
    md.drop_duplicates(inplace=True) #get rid of duplicate rows 

    for column in md:
        if column == 'unit':
            md[column] = md[column].str.split("unit/", expand=True).iloc[:,-1:]
        else: 
            md[column] = md[column].str.split("#", expand=True).iloc[:,-1:]

    # extract the ids from the metadata dataframe and add DATETIME
    md.set_index('sensorid', inplace=True, drop=True)
    ids = list(md.index)
    ids.insert(0,'DATETIME')

    # extract the location from the metadata dataframe 
    path = md['dblocation'][0]

    # retrieve timeseries data
    ts = get_ts_data(ids, path)
   
    return md, ts 

def get_ts_data(ids, path):
    """
    Retrieves timeseries data using the ids given
    Input: list containing timeseries ids
    Output: pandas dataframe containing timeseries data for given id's
    """
    ts = pd.read_csv(path, usecols=ids)
    ts['DATETIME'] = pd.to_datetime(ts['DATETIME'])
    ts.set_index('DATETIME', inplace=True, drop=True)
    return ts

def missing_values(ts):
    """
    Checks if the timeseries data contains missing values, and what percentage of data is missing
    Input: timeseries pandas dataframe  
    Output: pandas dataframe, indexed by column name
    """

    # row, column count 
    row, col = ts.shape

    # count empty values and percentage of column empty
    num_empty = ts.isnull().sum()
    percent_empty = 100 * num_empty / row
    
    # create a pandas table to store this information. Sort by percentage missing, descending order 
    mis_val_table = pd.concat([num_empty, percent_empty], axis=1).rename(columns = {0 : 'N. of Missing Values', 1 : '% of Values Missing'})
    mis_val_table = mis_val_table[mis_val_table.iloc[:,1] != 0].sort_values('% of Values Missing', ascending=False).round()
    
    print(f"The timeseries data has {col} columns. \n{len(mis_val_table.index)} of these have missing values.")
    
    return mis_val_table

def timeseries_plot(timeseries,metadata, sensors=None, timeslice=None):
    """ 
    Plots timeseries data for a given list of sensors and time period
    Inputs: timeseries data as pandas dataframe, a list of sensors, timeslice as a tuple (YY-MM-DD HH-MM-SS, YY-MM-DD HH-MM-SS)
    """

    if timeslice: 
        try:
            timeseries = timeseries[timeslice[0]:timeslice[1]]
        except:
            print("Timeslice is invalid. Must be of format ('YY-MM-DD HH-MM-SS', 'YY-MM-DD HH-MM-SS') ")
            return
    
    if sensors:
        try:
            timeseries = timeseries[sensors]
            
        except:
            print("Sensors are invalid. Must be strings in a list. Check the naming")
            return
    
    elif not sensors:
        sensors = list(timeseries.columns)
    
    sensor_units = {}
    for sensor in sensors:
        sensor_units[sensor] = metadata["unit"][sensor]

    if len(set(sensor_units.values())) != 1:
        # there is more than one unit 
        print("NOTE: Sensors are of different units")
        return

    timeseries.plot(xlabel= "Time-Stamp",ylabel=list(sensor_units.values())[0])
    plt.show()