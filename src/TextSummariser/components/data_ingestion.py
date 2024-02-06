import urllib.request as request
import zipfile
from TextSummariser.logging import logger
from TextSummariser.utils.common import get_size
from TextSummariser.entity import DataIngestionConfig
from pathlib import Path



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    
    def download_file(self):

        """
        Description: This function download zip filefrom given url

        Return: None


        """
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} downlaod! with following info: \n{headers}")
        else:
            logger.info(f"File alreay existof size {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        """
        Description: This function extract elements of a zi file.

        Return: None
        
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)    