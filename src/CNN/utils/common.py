# Those function which is used in multiple files are defined here

import os 
from logging import exception
from box.exceptions import BoxValueError
import yaml
from CNN import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import pickle


# First function which is nothing but read yaml 
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads Yaml file and returns 
    
    Args: 
        path_to_yaml (str): Path like input
        
    Raises: 
        ValueError: If yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """
    
    try: 
        with open(path_to_yaml, "r") as file: 
            content = yaml.safe_load(file)
            logger.info(f"Reading yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        logger.error(f"Error in reading yaml file: {e}")
        
        
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False"""
        
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data:dict):
    
    """Save json file
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")
    
    
@ensure_annotations
def load_json(path_to_load: Path) -> ConfigBox:
    """Load json file 
    Args: 
        path (Path):  path to json file 
        
    Returns:
        dict: data in json file
    """
    
    with open(path_to_load, 'r') as file:
        content = json.load(file)
        
    logger.info(f"json file loaded from: {path_to_load}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path:Path):
    """Save binary file
    
    Args:
        data(Any): Data to be saved as binary file
        path(Path): Path to save binary file
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")
    
    # Also we can use this code save binary file(Pickle)
    # with open(path, "wb") as file:
    #      pickle.dump(data, file)
    # logger.info(f"Binary file saved to: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file
    
    Args:
        path(Path): Path to binary file
        
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """Get size in kB
    
    Args:
        path(Path): Path to file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 3)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as file:
        file.write(imgdata)
        
        
def encodeImageIntBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')