from src.CNN import logger
from src.CNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNN.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.CNN.pipeline.stage_03_model_trainer import PrepareModelTrainer
from src.CNN.pipeline.stage_04_Evaluation import EvaluateModel


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

STAGE_NAME = "Training"
try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = PrepareModelTrainer()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n X============X")
except Exception as e:
        logger.exception(e)
        raise e 
    
    
STAGE_NAME = "Evaluation"
try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = EvaluateModel()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n X============X")
    
except Exception as e:
    logger.exception(e)
    raise e



