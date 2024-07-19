####################
# Standard Imports #
####################

from src.standard_imports import *

#################
# Local Imports #
#################


from src.html_renderable import HtmlRenderable


#########
# Class #
#########


class HtmlRawText(HtmlRenderable):
    def set_state(self, **kwargs):
        self.strings = []

    def add(self, arg):
        if isinstance(arg, str):
            self.strings.append(arg)
        super().add(arg)

    def build(self):
        return self.strings
