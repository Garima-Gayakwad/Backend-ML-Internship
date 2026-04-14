import logging
# Configure logging to save to task_manager.log
logging.basicConfig(
    filename="task_manager.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("TaskManager") # Create a logger object to use in other files