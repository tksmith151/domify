####################
# Standard Imports #
####################

from src.standard_imports import *

#################
# Local Imports #
#################


from src.html_attr import attr
from src.html_block import HtmlBlock, HtmlRenderable
from src.html_tag import tag



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