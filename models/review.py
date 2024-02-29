""" Module """
from . import base_model


class Review (base_model.BaseModel):
    """ Subclass """

    place_id = ''
    user_id = ''
    text = ''
