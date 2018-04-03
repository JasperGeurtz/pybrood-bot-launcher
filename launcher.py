### IMPORTS ###
import configparser
import os
import sys


### CUSTOM IMPORTS ###
import pybrood
import random
import time

### PATHS ###
bwapi_ai_path = "bwapi-data/AI/"
config_name = "scriptloader.ini"
sys_path = os.getcwd()


if __name__ == "__main__":
    if not os.path.isfile(config_name):
        config_name = bwapi_ai_path + config_name
        sys_path += "/" + bwapi_ai_path

    sys.path.insert(0, sys_path)

    config = configparser.ConfigParser()
    config.read(config_name)

    main = config["SCRIPT"]

    exec("import {}".format(main["filename"]))
    exec("pybrood.run({}.{})".format(main["filename"], main["classname"]))
