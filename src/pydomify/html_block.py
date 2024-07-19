####################
# Standard Imports #
####################

from src.pydomify.standard_imports import *

#################
# Local Imports #
#################


from src.pydomify.html_renderable import HtmlRenderable
from src.pydomify.html_text import HtmlText


#############
# Structure #
#############


class HtmlBlock(HtmlRenderable):
    def set_state(self, **kwargs):
        self.children: List[HtmlRenderable] = []

    def add(self, arg: Any):
        if isinstance(arg, HtmlRenderable):
            self.children.append(arg)
            return
        if isinstance(arg, str):
            self.children.append(HtmlText(arg))
            return
        super().add(arg)

    def build(self):
        output = []
        for child in self.children:
            output.extend(child.build())
        #if output and output[0] == "\n":
        #   output[0] = ""
        return output
