####################
# Standard Imports #
####################

from src.pydomify.standard_imports import *

#########
# Class #
#########

class HtmlRenderable(abc.ABC):
    #####################
    # Subclass Overides #
    #####################
    @abc.abstractmethod
    def set_state(self, **kwargs) -> None:
        """Initialize needed class state"""
        raise NotImplementedError

    def add(self, arg: Any) -> None:
        """Add provided argument object or raise NotImplementedError"""
        raise NotImplementedError(f"Cannot add type {type(arg)}")

    @abc.abstractmethod
    def build(self) -> List[str]:
        """Build list of strings structured by the renderable"""
        raise NotImplementedError

    ######################
    # Predefined Methods #
    ######################
    def __init__(self, *args, **kwargs) -> None:
        self.set_state(**kwargs)
        self.__call__(*args)

    def __call__(self, *args):
        for arg in args:
            self.add(arg)
        return self

    def __iadd__(self, arg):
        self.add(arg)
        return self

    def render(self):
        return "".join(self.build())
    
    def type_error(self, arg: Any):
        raise NotImplementedError(f"Cannot add type {type(arg)}")
