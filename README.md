## Implementing the Brick Ontology

This repository is part of Briana Davies-Morrell's honours thesis at the University of Western Australia. 

It contains an implementation of the Brick ontology for a pump manufacturer's HVAC system. The data used in this repository is an example only, manufactured for 
the purposes of confidentiality. This data can be found in the csv_files folder: example_metadata.csv is an Excel spreadsheet containing extracted HVAC metadata, and example_timeseries.csv contains the corresponding timeseries data.

Generate.py automatically creates a Brick model based on example_metadata.csv and compile.py performs reasoning on the Brick model, once created. Data_retrieval.ipynb demonstrates the use of a Brick model, and server.py opens an interactive server through which the Brick model can be queried. Extensions.py is used to extend the original Brick ontology where there are missing classes.

#### Getting Started

The dependencies for this project are listed in enviroment.yml. They can be installed by running:

```
conda env create -f environment.yml
conda activate env
```