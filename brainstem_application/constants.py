"""
constants.py

Stores the static, immutable, and specific data throughout the application
"""

import os

# Project Constants

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/.."
BRAINSTEM_APPLICATION_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = f"{ROOT_DIR}/data"
DATA_GENERATED_DIR = f"{DATA_DIR}/generated"
DATA_GENERATED_GENESET_DIR = f"{DATA_GENERATED_DIR}/geneset"

LOGS_DIR = f"{ROOT_DIR}/logs"

AMBA_ATLAS_IDS = {
    "Mouse, P56, Coronal": 1,
    "Mouse, P56, Sagittal": 2,
    "Developing Mouse, P4": 181276162,
}

AMBA_PRODUCT_IDS = {}
