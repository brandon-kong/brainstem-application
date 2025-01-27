""" Data Retrieval Service
This module contains the DataRetrievalService class, which is a service that retrieves data from a data source.
"""

from brainstem_application.services.base import Service


class DataRetrievalService(Service):
    def __init__(self):
        super().__init__("Data Retrieval Service")

    def docs(self):
        return "This service retrieves data from a data source."

    def startup(self):
        pass

    def cleanup(self):
        pass
