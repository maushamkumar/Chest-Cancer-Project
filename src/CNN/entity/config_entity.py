# This entity class is used to store the configuration of the data ingestion process.
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # Because of frozen=True, we can't change the values of the fields after the object is created
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path