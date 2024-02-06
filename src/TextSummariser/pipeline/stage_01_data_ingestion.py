from TextSummariser.config.configuration import ConfiguartionManager
from TextSummariser.components.data_ingestion import DataIngestion
from TextSummariser.logging import logger




class DataIngestionTrainingPipepline:
    def __init__(self):
        pass

    def main(self);
        config=ConfiguartionManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()