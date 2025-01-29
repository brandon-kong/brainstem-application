"""Service.py
This module contains the Service class, which is a base class for all services in the application.
"""


class Service:
    def __init__(self, name: str = "Unnamed Service"):
        if isinstance(name, str) == False:
            raise ValueError("[Service(init)]: name cannot be none")
        self.name = name

    def get_name(self):
        return self.name

    def docs(self):
        raise NotImplementedError("[Service(docs)]: docs not implemented")

    def startup(self):
        raise NotImplementedError("[Service(startup)]: startup not implemented")

    def cleanup(self):
        raise NotImplementedError("[Service(cleanup)]: cleanup not implemented")

    def __str__(self):
        return self.name
