import os
import unittest


from brainstem_application.services.data.data_retrieval_service import DataRetrievalService


class TestDataRetrievalService(unittest.TestCase):

    def test_service_name(self):
        service = DataRetrievalService()
        self.assertEqual(service.get_name(), "Data Retrieval Service")
