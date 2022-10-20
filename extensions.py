import brickschema
from brickschema.namespaces import BRICK, RDFS
from rdflib import Namespace

#################################################################################
# Extensions to the Brick ontology 
#################################################################################

# A graph to hold the model
g = brickschema.Graph()

# A namespace to hold Brick extensions. bind it to g
# namespace =  set of names for a particular purpose 
EXT = Namespace('urn:extension#')
g.bind("ext", EXT)
g.bind("brick", BRICK)
g.bind("rdfs", RDFS)

# Create connector and header classes 
g.add((EXT['Connecting_Pipe'], RDFS.subClassOf, BRICK["HVAC_Equipment"]))
g.add((EXT['Header'], RDFS.subClassOf, EXT['Connecting_Pipe']))

g.serialize("./brick_model/ttl_files/brick_extension.ttl", format="ttl")
