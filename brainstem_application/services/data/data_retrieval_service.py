"""Data Retrieval Service
This module contains the DataRetrievalService class, which is a service that retrieves data from a data source.
"""

import requests
from typing import Optional
from pydantic import BaseModel

from services.base import Service


class Gene(BaseModel):
    acronym: str
    alias_tags: Optional[str] = None
    chromosome_id: Optional[int] = None
    ensembl_id: Optional[str] = None
    entrez_id: Optional[int] = None
    genomic_reference_update_id: Optional[int] = None
    homologene_id: Optional[int] = None
    id: int
    legacy_ensembl_gene_id: Optional[str | int] = None
    name: str
    organism_id: int
    original_name: str
    original_symbol: str
    reference_genome_id: Optional[str | int] = None
    sphinx_id: int
    version_status: Optional[str] = None

class DataRetrievalService(Service):
    def __init__(self):
        super().__init__("Data Retrieval Service")

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
                    f"An error occurred while retrieving the gene set from the product 1: {data['msg']}"
                )
                return None
            
            return [Gene(**gene) for gene in data["msg"]]
        except Exception as e:
            print(
                f"An error occurred while retrieving the gene set from the product 2: {e}"
            )
            return None

    def docs(self):
        return "This service retrieves data from a data source."

    def startup(self):
        pass

    def cleanup(self):
        pass
