#!/usr/bin/python3
"""The Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements a Review model"""
    place_id = ""
    user_id = ""
    text = ""
