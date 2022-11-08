import torch
import yaml

class SavePoint():
    def __init__(self, loaded_dict:dict):
        self.weights = loaded_dict['model']
        self.optim = loaded_dict['optim']
        self.args = loaded_dict['args']
        self.save_time = loaded_dict['save_time']

def load_savepoint(config_path:str) -> SavePoint:
    with open(config_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    savepoint = torch.load(config["model_path"], map_location='cpu')
    return SavePoint(savepoint)