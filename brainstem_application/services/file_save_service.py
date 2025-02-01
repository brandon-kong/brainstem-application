"""File Save Service
This module contains the FileSaveService class, which is a service that saves data to a file.
"""

import os
import requests
from typing import Optional
from pydantic import BaseModel

from constants import DATA_GENERATED_GENESET_DIR

from services.base import Service


class FileSaveService(Service):
    def __init__(self):
        super().__init__("Data Retrieval Service")

    @staticmethod
    def create_directory_if_not_exists(directory: str):
        """
        Create a directory if it does not exist
        """
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    def save_geneset_to_file(genes: list, file_name: str):
        """
        Save genes to a file
        """
        FileSaveService.create_directory_if_not_exists(DATA_GENERATED_GENESET_DIR)

        new_path = f"{DATA_GENERATED_GENESET_DIR}/{file_name}"

        with open(f"{new_path}", "w") as file:
            for gene in genes:
                file.write(f"{gene.acronym}\n")

        print(f"Genes exported to {new_path}")

    def docs(self):
        return "This service retrieves data from a data source."

    def startup(self):
        pass

    def cleanup(self):
        pass
