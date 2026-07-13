"""
logger.py
---------
Centralized logging configuration for the Employee API.
Logs to both console and logs/application.log.
"""

import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/application.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("employee_api")