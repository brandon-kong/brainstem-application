import os
import unittest


from brainstem_application.services.base import Service


class TestBaseService(unittest.TestCase):

    def test_service_name(self):
        service = Service("Test Service")
        self.assertEqual(service.get_name(), "Test Service")

    def test_invalid_service_name(self):
        with self.assertRaises(ValueError):
            Service(None)

    def test_docs(self):
        service = Service("Test Service")
        with self.assertRaises(NotImplementedError):
            service.docs()

    def test_startup(self):
        service = Service("Test Service")
        with self.assertRaises(NotImplementedError):
            service.startup()

    def test_cleanup(self):
        service = Service("Test Service")
        with self.assertRaises(NotImplementedError):
            service.cleanup()

    def test_str(self):
        service = Service("Test Service")
        self.assertEqual(str(service), "Test Service")
