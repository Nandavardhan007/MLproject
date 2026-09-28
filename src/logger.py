# import logging
# import os
# from datetime import datetime

# log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(),"logs",log_file)
# os.makedirs(logs_path,exist_ok=True)

# log_file_path = os.path.join(logs_path,log_file)

# logging.basicConfig(
#     filename=log_file_path,
# #    format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s",
#     format="[%(asctime)s] - %(lineno)d %(name)s - %(levelname)s - %(message)s",
     
#     level=logging.INFO,
# )

# if __name__ == "__main__":
#     # try :
#     #     a=1/0
#     # except Exception as e:
#     #     raise CustomEx
#     logging.info("Logging is started")
import logging
import os
from datetime import datetime


# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Create logs directory
LOG_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_PATH, exist_ok=True)


# Complete log file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)


# Configure logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)


# Create logger object
logger = logging.getLogger(__name__)