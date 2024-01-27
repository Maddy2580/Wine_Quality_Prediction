import os
import sys
import logging
from datetime import datetime

name = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir= "logs"
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_filepath = os.path.join(log_dir,log_file)
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= name,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger= logging.getLogger("WineQualityLogger")