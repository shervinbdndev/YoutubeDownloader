import json
import os 

def LoadCFG(filename):
    cfg_file = open(filename)
    cfg = json.load(cfg_file)
    cfg_file.close()
    return cfg

def SaveCFG(cfg, filename="cfg.json"):
    cfg_file = open(filename, "w+")
    json.dump(cfg, cfg_file)
    cfg_file.close()

def init(dconfig, filename="cfg.json"):
    if not os.path.isfile(filename):
        cfg_file = open(filename, "w+")        
        json.dump(dconfig, cfg_file)
        cfg_file.close()
        return LoadCFG(filename=filename)
    else:
        return LoadCFG(filename)