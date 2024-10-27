from src.CNN.config.configuration import ConfigurationManager
from src.CNN.components.Evaluation import Evaluation
from src.CNN import logger


STAGE_NAME = "Evaluation"

class EvaluateModel:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()         # Runs the model evaluation
        evaluation.log_into_mlflow()
        
if __name__ == "__main__":
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = EvaluateModel()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\n X============X")
    except Exception as e:
        logger.exception(e)
        raise e 
        