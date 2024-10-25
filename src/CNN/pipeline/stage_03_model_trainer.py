from src.CNN.config.configuration import ConfigurationManager
from src.CNN.components.model_trainer import Training
from src.CNN import logger

STAGE_NAME = "Training"

class PrepareModelTrainer:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
        
if __name__ == "__main__":
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = PrepareModelTrainer()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n X============X")
    except Exception as e:
        logger.exception(e)
        raise e 
        