import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'mlProject'


list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]


for filepath in list_of_files:
    filepath = Path(filepath)  #detect our os and create path accordingly
    filedir, filename = os.path.split(filepath) #split the path into directory and file name
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) #create the directory if it does not exist
        logging.info(f"Creating directory: {filedir} for file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #create an empty file
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")