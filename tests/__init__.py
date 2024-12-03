import json
from pathlib import Path

import fractal_olympus_converter

PACKAGE = "fractal_olympus_converter"
PACKAGE_DIR = Path(fractal_olympus_converter.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]