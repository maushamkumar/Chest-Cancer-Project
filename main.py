from src.CNN import logger
from src.CNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNN.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try: 
    logger.info(f" >>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f" >>>>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n Next ====================== RUN")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n X============X")
        
except Exception as e:
    logger.exception(e)
    raise e 
    