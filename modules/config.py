import os
from dataclasses import dataclass


@dataclass
class ModelPredictionConfig:

    swh_file_path = os.path.join("FOLDER_NAME", "FILE_NAME")
