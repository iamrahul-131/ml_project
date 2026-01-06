import sys
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    exception_file_name=exc_tb.tb_frame.f_code.co_filename##tells in which file exception occured basically tells the file name
    exception_line=exc_tb.tb_lineno##at which line number exception occured
    exception_error=str(error)#what is error message when exception occured 
    error_message="Error occurd in python script name [{0}] line number [{1}] error message[{2}]".format()
    exception_file_name,exception_line,exception_error

    return error_message

class CustomException(Exception):
    def _init__(self,error_message,error_detail:sys): #Constructor
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)