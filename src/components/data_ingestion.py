import os
import sys
#the reason we are importing above two in order to use custom exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path:  str=os.path.join('artifacts',"test.csv")
    raw_data_path:   str=os.path.join('artifacts',"data.csv")
# If you have to only define class variable then decorator is a good option but if you want to define variable and function both then use __init__ function only.
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#this ingestion_cinfig will consist of two three values 

    def initiate_data_ingestion(self):#if my data is in databases then i will write my code to read from database but initially read the dataset in a very easy way.
        logging.info("Enter the data ingestion method or component")
        try:#here only we have to write code in order to read data from any databases but right now taking onlt stud.csv which i have uploaded in my notebook folder
            df=pd.read_csv(r"Notebook\data\stud.csv")
            logging.info("Read the dataset as DataFrame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)#raw data ko artifact folder mae save kar rha aur csv mae convert kar rha hai

            logging.info("Train test splitted initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#train data ko artifact folder mae save kar rha hai aur csv mae convert kar rha hai

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#test data ko artifact folder mae save kar rha hai aur csv mae convert kar rha hai

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path   #now we are returning these two things because in order to do data transformation where these two information will be passed which is trainig data path and test data path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

