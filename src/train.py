import yaml 
import sys
import numpy as np
import pandas as pd
import argparse
from typing import Text
import joblib

sys.path.append('/home/bigpenguin/projects/dvc/')

# my modules
from models import train

def train_model(config_path: Text) -> None:

    '''
    loading params
    '''
    with open('params.yaml') as conf_file:
        config = yaml.safe_load(conf_file)
    
    train_df = pd.read_csv(config['data_split']['trainset_path'])

    model = train(train_df)
    models_path = config['train']['model_path']
    joblib.dump(model, models_path)



if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    train_model(config_path=args.config)
