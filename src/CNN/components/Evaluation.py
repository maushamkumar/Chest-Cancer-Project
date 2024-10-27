import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from mlflow.models import infer_signature
from src.CNN.utils.common import read_yaml, create_directories, save_json
from src.CNN.entity.config_entity import EvaluationConfig
import os 
import dagshub

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        
    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
        


    def log_into_mlflow(self):
        # Initialize DagsHub repository
        dagshub.init(repo_owner='maushamkumar', repo_name='Chest-Cancer-Project', mlflow=True)

        # Set environment variables
        os.environ['MLFLOW_TRACKING_URI'] = self.config.mlflow_uri
        os.environ['MLFLOW_TRACKING_TOKEN'] = "840e97a11ba7812e407d7188fc60a602455a3cbb"
    
        # os.environ['MLFLOW_TRACKING_USERNAME'] = 'Mausham-Kumar'
        # os.environ['MLFLOW_TRACKING_PASSWORD'] = '840e97a11ba7812e407d7188fc60a602455a3cbb'

        # Print the environment variables for debugging
        print("MLFLOW_TRACKING_URI:", os.environ.get('MLFLOW_TRACKING_URI'))
        print("MLFLOW_TRACKING_USERNAME:", os.environ.get('MLFLOW_TRACKING_USERNAME'))
        print("MLFLOW_TRACKING_PASSWORD:", os.environ.get('MLFLOW_TRACKING_PASSWORD'))

        mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})

            # Ensure the model is not None and is a Keras model
            if self.model is None or not isinstance(self.model, tf.keras.Model):
                print("Model is not loaded correctly.")
                return

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")
