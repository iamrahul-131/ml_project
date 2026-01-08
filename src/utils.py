import os
import sys
import numpy as np
import pandas as pd
import dill #it is another library used to create pickle file
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score 


from src.exception import CustomException

def save_object(file_path,obj):## this function is used to save preprocessor object as a pickle file
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True) 

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        

    except Exception as e:
        raise CustomException(e,sys)
    

from sklearn.metrics import r2_score
import sys

def evaluate_models(x_train, y_train, x_test, y_test, models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs=GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)


            # Train model
            #model.fit(x_train, y_train)

            # Predictions
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            # Scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Store test score
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise Exception(e)
    
def load_object(file_path):#basicslly it is opening model_path in read mode and uploading model in pickle format where load_object function is called
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)
