import os
import sys
from src.exceptions import CustomExcpetion
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass
from src.utils import evaluate_models

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import (AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor)

from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1],
            )
            #create a dictioner for all the models
            models = {
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "XGBoost Regressor": XGBRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "Gradient Boosting Regressor": GradientBoostingRegressor(),
            }
            

            model_report: dict = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models
            )

            logging.info(f"Model report: {model_report}")

            # Find the model with the highest R2 score
            best_model_name = max(
                model_report,
                key=model_report.get
            )

            # Get the corresponding score
            best_models_score = model_report[best_model_name]

            # Get the actual model
            best_model = models[best_model_name]

            logging.info(
                f"Best model: {best_model_name}"
            )

            logging.info(
                f"Best model R2 score: {best_models_score}"
            )

            if best_models_score < 0.6:
                raise CustomExcpetion("No best model found")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_score_ = r2_score(
                y_test,
                predicted
            )

            logging.info(
                f"Final R2 score: {r2_score_}"
            )

            return r2_score_,best_model
        except Exception as e :
            raise CustomExcpetion(e,sys)
        
