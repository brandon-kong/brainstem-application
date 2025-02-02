"""Data Retrieval Service
This module contains the DataRetrievalService class, which is a service that retrieves data from a data source.
"""

import requests
from typing import Optional
from pydantic import BaseModel

from services.base import Service

from models import Gene, SectionDataSet

class DataRetrievalService(Service):
    def __init__(self):
        super().__init__("Data Retrieval Service")

    @staticmethod
    def get_section_dataset_ids_with_reference_space_id(reference_space_id: int, delegate: bool = True, should_contain_genes: bool = True):
        """
        Get a section dataset ID with a reference space ID
        """
        try:
            response = requests.get(
                f"http://api.brain-map.org/api/v2/data/SectionDataSet/query.json?criteria=reference_space[id$eq{reference_space_id}]&num_rows=all&include=genes"
            )
            data = response.json()

            if not "msg" in data:
                print(
                    f"An error occurred while retrieving the section dataset ID with the reference space: {data['msg']}"
                )
                return None
                
            data = [SectionDataSet(**section) for section in data["msg"]]

            if delegate:
                data = [section for section in data if section.delegate]

            if should_contain_genes:
                data = [section for section in data if section.genes is not None and len(section.genes) > 0] 

            return data
        except Exception as e:
            print(
                f"An error occurred while retrieving the section dataset ID with the reference space: {e}"
            )
            return None
        
    @staticmethod
    def get_geneset_from_product(product_id: int):
        """
        Get a gene set from a product
        """
        try:
            response = requests.get(
                f"http://api.brain-map.org/api/v2/data/Gene/query.json?criteria=products[id$eq{product_id}]&num_rows=all"
            )
            data = response.json()

            if not "msg" in data:
                print(
                    f"An error occurred while retrieving the gene set from the product: {data['msg']}"
                )
                return None
            
            return [Gene(**gene) for gene in data["msg"]]
        except Exception as e:
            print(
                f"An error occurred while retrieving the gene set from the product: {e}"
            )
            return None

    def docs(self):
        return "This service retrieves data from a data source."

    def startup(self):
        pass

    def cleanup(self):
        pass
