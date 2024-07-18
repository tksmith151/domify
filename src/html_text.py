####################
# Standard Imports #
####################

from src.standard_imports import *

#################
# Local Imports #
#################


from src.html_raw_text import HtmlRawText


#############
# Structure #
#############


class HtmlText(HtmlRawText):
    def add(self, arg) -> None:
        if isinstance(arg, str):
            self.strings.append(html.escape(arg))
            return
        super().add(arg)
