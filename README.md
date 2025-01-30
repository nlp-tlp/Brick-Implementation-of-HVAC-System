## Implementing the Brick Ontology

This repository is part of Briana Davies-Morrell's honours thesis at the University of Western Australia. 

It contains an implementation of the Brick ontology for a pump manufacturer's HVAC system. The data used in this repository is an example only, manufactured for 
the purposes of confidentiality. This data can be found in the csv_files folder: example_metadata.csv is an Excel spreadsheet containing extracted HVAC metadata, and example_timeseries.csv contains the corresponding timeseries data.

### Getting Started

The dependencies for this project are listed in enviroment.yml. They can be installed by running:

```
conda env create -f environment.yml
conda activate env
```

Alternatively, you can set-up a virtual environment by:
1. Create a venv: ```python -m venv venv```
2. Activate the venv: ```venv/scripts/activate```
3. Install the requirements: ```pip install -r requirements.txt```

### Running the Files in the Repository
1. ```python generate.py``` - creates a Brick model based on example_metadata.csv
2. ```python compile.py``` - performs reasoning on the Brick model
3. Navigate to Data_retrieval.ipynb - this jupyter notebook demonstrates the use of the Brick model for data retrieval
4. ```python server.py``` - opens an interactive server through which the Brick model can be queried
5. ```python extensions.py``` - used to extend the original Brick ontology where there are missing classes
