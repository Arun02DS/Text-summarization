import os
import yaml
from box.exceptions import BoxValueError
from TextSummariser.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any




@ensure_annotations
def read_yaml(file_path_yaml:Path)->ConfigBox:
    """
    Description: This function reads yaml file.

    Return: configbox type

    """
    try:
        with open(file_path_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Description: This function creates directories from a list of directories.

    Return : None

    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def get_size(path:Path)->str:
    """
    Description: This function manupulate the size in kb

    Return: string size in kb
    
    """

    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kB"