import os 
import sys
import logging

logging_str = "[%(asctime)s :%(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logs.log")  # This will save all the logs 
os.makedirs(log_dir, exist_ok=True) # Here we are creating floder

logging.basicConfig(  # Here we are define logging configuration 
    level=logging.INFO, 
    format=logging_str, 
    
    handlers=[
    logging.FileHandler(log_filepath), # It will save log inside the folder. 
    logging.StreamHandler(sys.stdout) # This will print that log in terminal itself. 
    ]
)

logger = logging.getLogger('CNNLogger') # Call your logger.