import sys

from network_security.logging import logger
class NetworkSecurityError(Exception):
    """Base exception for network security errors."""
    def __init__(self,error_message,error_details:sys) -> None:
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
        
        
        def __str__(self) -> str:
            return f'Error occured in script: {self.filename} at line number: {self.lineno} error message: {self.error_message}'
        
        
if __name__ == "__main__":
    try:
        logger.logging.info("Entered the try block of exception.py")
        a = 1/0
    except Exception as e:
        raise NetworkSecurityError(e,sys)