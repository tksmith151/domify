####################
# Standard Imports #
####################

from src.pydomify.standard_imports import *

#################
# Local Imports #
#################


from src.pydomify.html_attr import attr
from src.pydomify.html_block import HtmlBlock, HtmlRenderable
from src.pydomify.html_tag import tag



#############
# Structure #
#############


class HtmlPage(HtmlRenderable):
    def set_state(self):
        self.page = HtmlBlock()
        self.page.add(tag.doctype(attr.html))

    def add(self, arg) -> None:
        self.page.add(arg)

    def build(self):
        return self.page.build()