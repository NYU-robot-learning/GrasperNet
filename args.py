import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode",
                    choices = ["mv", "pi"], default = "m",
                    help = "Choose the mode of operation."
                            "m  -> moving about a frame of reference to a point"
                            "po -> Picking a object with fixed offset")
    parser.add_argument("-bf", "--base_frame",
                    choices = ["gc", "tc"], default = "gc",
                    help = "Operating frame of reference")
    parser.add_argument("-t", "--transform", 
                    action="store_true", 
                    help = "Boolean for transforming a input co-ordinates to another frame of reference")
    parser.add_argument("-tf", "--transform_node", 
                    choices = ["gc", "tc", "gl", "gr"], default = "gl",
                    help = "Operating frame of reference")
    
    return parser.parse_args()