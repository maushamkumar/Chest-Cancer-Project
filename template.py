import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(message)s:') # This will print time stand and log message

project_name = "CNN"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components.py/__init__.py",
    f"src/{project_name}/utils.py/__init__.py",
    f"src/{project_name}/config.py/__init__.py",
    f"src/{project_name}/config.py/configuration.py",
    f"src/{project_name}/pipeline.py/__init__.py",
    f"src/{project_name}/entity.py/__init__.py",
    f"src/{project_name}/constants.py/__init__.py",
    "config/config.yml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            logging.info(f"Creating file: {filename}")
            pass
            logging.info(f"Creating empty file: {filename}")
            
    else:
        logging.info(f"File: {filename} already exists")