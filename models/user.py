#!/usr/bin/python3
"""The user's model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class and add user's functionalities

    Args:
        email (str): His email 
        password (str): His password 
        first_name (str): His first name 
        last_name (str): His last name 
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
