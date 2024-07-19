#################
# Local Imports #
#################


from src.pydomify.html_attribute import HtmlAttribute


######################
# Dynamic Attributes #
######################


class Content(HtmlAttribute):
    def __init__(self, value) -> None:
        super().__init__("content", value)


class Href(HtmlAttribute):
    def __init__(self, value) -> None:
        super().__init__("href", value)


class Id(HtmlAttribute):
    def __init__(self, value) -> None:
        super().__init__("id", value)


class Src(HtmlAttribute):
    def __init__(self, value) -> None:
        super().__init__("src", value)


#####################
# Static HtmlAttributes #
#####################


class Charset:
    def __init__(self) -> None:
        name = "charset"
        self.utf8 = HtmlAttribute(name, "utf-8")


class HxBoost:
    def __init__(self) -> None:
        name = "hx-boost"
        self.true = HtmlAttribute(name, "true")


class Lang:
    def __init__(self) -> None:
        name = "lang"
        self.en = HtmlAttribute(name, "en")


class Name:
    def __init__(self) -> None:
        name = "name"
        self.description = HtmlAttribute(name, "description")
        self.keywords = HtmlAttribute(name, "keywords")
        self.viewport = HtmlAttribute(name, "viewport")


class Rel:
    def __init__(self) -> None:
        name = "rel"
        self.icon = HtmlAttribute(name, "icon")
        self.stylesheet = HtmlAttribute(name, "stylesheet")


class Type:
    def __init__(self) -> None:
        name = "type"
        self.button = HtmlAttribute(name, "button")
        self.icon = HtmlAttribute(name, "image/x-icon")
        self.module = HtmlAttribute(name, "module")


class Attr:
    def __init__(self) -> None:
        # Dynamic HtmlAttributes
        self.content = Content
        self.href = Href
        self.id = Id
        self.src = Src
        # Static HtmlAttributes
        self.charset = Charset()
        self.hx_boost = HxBoost()
        self.lang = Lang()
        self.name = Name()
        self.rel = Rel()
        self.type = Type()

    @property
    def defer(self):
        return HtmlAttribute("defer")

    @property
    def html(self):
        return HtmlAttribute("html")


attr = Attr()
