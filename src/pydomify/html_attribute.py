####################
# Standard Imports #
####################

from src.standard_imports import *


#############
# Structure #
#############


class HtmlAttribute:
    """Class for HTML Attributes"""
    def __init__(self, key: str, value: str = None) -> None:
        self.key = key
        self.value = value
