import os
import sys
import pickle as dill
import pandas as pd
import numpy as np
from src.exceptions import CustomExcpetion
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok= True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            # .dump file_path.readlines
            pass
        
    except CustomExcpetion as e:
        raise(e,sys)
        