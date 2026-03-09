from app.services.facade import HBnBFacade
"""This facade instance will be used as a singleton to make sure that only
one instance of the HBnBFacade class is created
and used throughout the application"""
facade = HBnBFacade()
