# This entity class is used to store the configuration of the data ingestion process.
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # Because of frozen=True, we can't change the values of the fields after the object is created
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int