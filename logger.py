import logging
import os
from datetime import datetime

# Setting up logging configuration
# This will create a log file with the current date and time in the logs directory

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path for the logs directory
log_path=os.path.join(os.getcwd(),"logs")

# Create the logs directory if it does not exist
os.makedirs(log_path,exist_ok=True)

# Define the full path for the log file
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

# Configure the logging
logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)
