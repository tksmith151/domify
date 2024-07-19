####################
# Standard Imports #
####################


from src.pydomify.standard_imports import *


#################
# Local Imports #
#################


from src.pydomify.html_attribute import HtmlAttribute
from src.pydomify.html_block import HtmlBlock


#############
# Structure #
#############


class HtmlElement(HtmlBlock):
    def set_state(self, **kwargs):
        self.name: str = kwargs.get("name")
        self.close: bool = kwargs.get("close", True)
        self.attributes: Dict[str,List[str]] = {}
        super().set_state(**kwargs)

    def add(self, arg: any):
        if isinstance(arg, HtmlAttribute):
            attribute: HtmlAttribute = arg
            self.attributes.setdefault(attribute.key, [])
            if attribute.value:
                self.attributes[attribute.key].append(attribute.value)
            return
        super().add(arg)

    def build(self):
        output = []
        output.append("<")
        output.append(self.name)
        for key, values in self.attributes.items():
            output.append(" ")
            output.append(key)
            if len(values) > 0:
                output.append('="')
                output.extend(values)
                output.append('"')
        output.append(">")
        output.extend(super().build())
        if self.close:
            output.extend(["</", self.name, ">"])
        return output
