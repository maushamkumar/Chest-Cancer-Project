from src.CNN import logger
from src.CNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try: 
    logger.info(f" >>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f" >>>>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n Next ====================== RUN")
    
except Exception as e:
    logger.exception(e)
    raise e