from brickschema import Graph

g = Graph().load_file("./brick_model/ttl_files/example_compiled_bldg.ttl")
g.serve("localhost:8080") 