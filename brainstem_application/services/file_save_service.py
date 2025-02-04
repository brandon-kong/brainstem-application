"""File Save Service
This module contains the FileSaveService class, which is a service that saves data to a file.
"""

import io
import os
import zipfile
import requests
from typing import Optional
from pydantic import BaseModel

from constants import DATA_GENERATED_GENESET_DIR, DATA_TEMP_DIR, DATA_GENERATED_SECTION_DATASET_DIR

from services.base import Service


class FileSaveService(Service):
    def __init__(self):
        super().__init__("Data Retrieval Service")

    @staticmethod
    def save_section_dataset_ids_to_file(section_dataset_ids: list[int], file_name: str):
        """
        Save section dataset IDs to a file
        """
        FileSaveService.create_directory_if_not_exists(DATA_GENERATED_SECTION_DATASET_DIR)

        new_path = f"{DATA_GENERATED_SECTION_DATASET_DIR}/{file_name}"

        with open(f"{new_path}", "w") as file:
            for section_dataset_id in section_dataset_ids:
                file.write(f"{section_dataset_id}\n")

        print(f"Section dataset IDs exported to {new_path}")

    @staticmethod
    def unzip_grid_expression_data(grid_expression_data: bytes, path: str = DATA_TEMP_DIR):
        """
        Unzip grid expression data
        """
        FileSaveService.create_directory_if_not_exists(path)

        with zipfile.ZipFile(grid_expression_data, 'r') as zip_ref:
            zip_ref.extractall(path)
        
    @staticmethod
    def save_grid_expression_data_to_file(grid_expression_data: bytes, file_name: str):
        """
        Save grid expression data to a file
        """
        FileSaveService.create_directory_if_not_exists(DATA_TEMP_DIR)

        new_path = f"{DATA_TEMP_DIR}/{file_name}"

        new_zip = zipfile.ZipFile(new_path, 'w')
        new_zip.write(grid_expression_data)
        new_zip.close()


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
