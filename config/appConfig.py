import os
from pathlib import Path


ROOT_PATH: str = Path(__file__).parent.parent

ENV_FILE_PATH = os.path.join(ROOT_PATH, 'env.ini')
