"""
utility functions used for overland flow use case
"""
import os


# installation function
def install_api_key():
    work_dir = os.getcwd()

    # create Topography API key file
    topo_key = input("Enter Your OpenTopography API Key: ")
    topo_config_path = os.path.join(work_dir, ".opentopography.txt")

    with open(topo_config_path, "w") as topo_config_file:
        topo_config_file.write(topo_key)
    print(f"OpenTopography API Key file is created at {topo_config_path}.")
