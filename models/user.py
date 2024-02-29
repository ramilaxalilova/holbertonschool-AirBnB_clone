"""
    Module
"""
from . import base_model


class User (base_model.BaseModel):
    """ Subclass """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
