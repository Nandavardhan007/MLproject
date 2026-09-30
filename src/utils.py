import os
import sys
import pickle as dill
import pandas as pd
import numpy as np
from src.exceptions import CustomExcpetion
from src.logger import logging
from sklearn.metrics import r2_score

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
def evaluate_models(X_train, y_train, X_test, y_test, models):

    try:

        report = {}

        for model_name, model in models.items():

            # Train model
            model.fit(X_train, y_train)

            # Predictions
            y_test_pred = model.predict(X_test)

            # R2 score
            test_model_score = r2_score(
                y_test,
                y_test_pred
            )

            # Store score
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomExcpetion(e, sys)
# def evaluate_models(X_train,y_train,X_test,y_test,models):
    report = {}
    try:
        for i in models:
            model = list(models.values())[i]
                
            model.fit(X_train,y_train)
                
            y_train_pred = model.predict(X_train)
            y_test_pred  = model.predict(X_test)
                
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
    
    except Exception as e:
        raise CustomExcpetion(e,sys)
    