import brickschema
from brickschema.namespaces import A, BRICK, UNIT, RDF, RDFS
from rdflib import Namespace, Literal
import pandas as pd

#################################################################################
# Create a Brick model
#################################################################################

def create_brick(model_path, timeseries_path, output_filename):
    """
    Function to create a Brick model from the Brick ontology. 
    Inputs: model_path = path to csv file with metadata information (str), timeseries_path = path to timeseries data (str), output_filename = name of the output ttl file
    Output: saves a file by filename given
    """

    g = brickschema.Graph().load_file("./brick_model/ttl_files/brick_extension.ttl")

    EXT = Namespace('urn:extension#')
    BLDG = Namespace("urn:mybuilding#")
    g.bind("bldg", BLDG)
    g.bind("rdfs", RDFS)
    g.bind("ext", EXT)
    
    # create an instance of a database, and link to the timeseries_path given
    g.add((BLDG['db'], A, BRICK['Database']))
    g.add((BLDG['db'], RDFS.label, Literal("Location of Timeseries Storage")))
    g.add((BLDG['db'], BRICK['connString'], Literal(timeseries_path)))

    # read in the model instances in model_path
    instances = pd.read_csv(model_path)

    # iterate through the instances and add to the brick model
    for _, row in instances.iterrows():

        row.str.strip(to_strip = None)

        g.add((BLDG[row['Name']], RDFS.label, Literal(row['Name'])))

        if row['Class_Type'] == 'Equipment':

            if row['Namespace'] == 'BRICK':
                g.add((BLDG[row['Name']], A, BRICK[row['Brick_Type']]))

            elif row['Namespace'] == 'EXT':
                g.add((BLDG[row['Name']], A, EXT[row['Brick_Type']]))

        elif row['Class_Type'] == 'Sensor':

            g.add((BLDG[row['Name']], A, BRICK[row['Brick_Type']]))
            g.add((BLDG[row['Name']], BRICK['isPointOf'], BLDG[row['Location']]))
            g.add((BLDG[row['Name']], BRICK['hasUnit'], UNIT[row['Unit']]))
            timeseries_props = [
                (BRICK['hasTimeseriesId'], Literal(row['ID'])),
                (BRICK['storedAt'], BLDG['db'])
            ]
            g.add((BLDG[row['Name']], BRICK['timeseries'], timeseries_props))

    # save file
    print('Finished. Brick model created and saved to ttl_files folder.')
    g.serialize(f"./brick_model/ttl_files/{output_filename}.ttl", format="ttl")

model_path = './brick_model/csv_files/example_metadata.csv'
timeseries_path = './csv_files/example_timeseries.csv'
output_filename = 'example_bldg'

create_brick(model_path, timeseries_path, output_filename)
