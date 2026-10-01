import os
import sys
import pickle as dill
import pandas as pd
import numpy as np
from src.exceptions import CustomExcpetion
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

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
def evaluate_models(X_train, y_train, X_test, y_test, models,params):

    try:

        report = {}

        for model_name, model in models.items():
            model_params = params[model_name]
            param_grid = {
                param_name: values
                if isinstance(values, (list, tuple, np.ndarray))
                else [values]
                for param_name, values in model_params.items()
            }
            search = GridSearchCV(
                estimator=model,
                param_grid=param_grid,
                cv=3,
                scoring="r2",
                 
                n_jobs=-1,
            )
            search.fit(X_train, y_train)

            logging.info(
                f"Best parameters for {model_name}: {search.best_params_}"
            )
            models[model_name] = search.best_estimator_

            # Evaluate the refitted best estimator on the held-out test data.
            y_test_pred = models[model_name].predict(X_test)

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
    
def load_object(file_path):
    try: 
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomExcpetion(e,sys)
        
# # def evaluate_models(X_train,y_train,X_test,y_test,models):
#     report = {}
#     try:
#         for i in models:
#             model = list(models.values())[i]
                
#             model.fit(X_train,y_train)
                
#             y_train_pred = model.predict(X_train)
#             y_test_pred  = model.predict(X_test)
                
#             train_model_score = r2_score(y_train, y_train_pred)
#             test_model_score = r2_score(y_test, y_test_pred)
            
#             report[list(models.keys())[i]] = test_model_score
    
#     except Exception as e:
#         raise CustomExcpetion(e,sys)
    