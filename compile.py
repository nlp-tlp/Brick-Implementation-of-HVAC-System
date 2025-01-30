import brickschema

#################################################################################
# Performing Reasoning on aBrick model
#################################################################################

# The Brick model to compile
model_path = './ttl_files/example_bldg.ttl'

# Most recent version of the Brick ontology  
bldg = brickschema.Graph(load_brick=True)

# Load in building specific instances to the Brick ontology  
bldg.load_file('./ttl_files/example_bldg.ttl')

# Compile the graph 
bldg.expand("brick")

# Save compiled graph
bldg.serialize('./ttl_files/example_compiled_bldg.ttl', format="ttl")

print('Finished. Brick model has been compiled and saved to ttl_files folder.')