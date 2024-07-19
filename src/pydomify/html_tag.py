####################
# Standard Imports #
####################


from src.pydomify.standard_imports import *


#################
# Local Imports #
#################


from src.pydomify.html_element import HtmlElement


############
# Property #
############

def HtmlElementProperty(name, *, close=True):
    @property
    def prop(self):
        return HtmlElement(name=name, close=close)

    @prop.setter
    def prop(self, value):
        raise NotImplementedError

    return prop

#######
# Tag #
#######

class Tag:
    ########
    # Root #
    ########
    doctype = HtmlElementProperty("!DOCTYPE", close=False)
    html = HtmlElementProperty("html")
    ############
    # Metadata #
    ############
    base = HtmlElementProperty("base", close=False)
    head = HtmlElementProperty("head")
    link = HtmlElementProperty("link", close=False)
    meta = HtmlElementProperty("meta", close=False)
    noscript = HtmlElementProperty("noscript")
    script = HtmlElementProperty("script")
    style = HtmlElementProperty("style")
    title = HtmlElementProperty("title")
    ############
    # Sections #
    ############
    address = HtmlElementProperty("address")
    article = HtmlElementProperty("article")
    aside = HtmlElementProperty("aside")
    body = HtmlElementProperty("body")
    footer = HtmlElementProperty("footer")
    header = HtmlElementProperty("header")
    hgroup = HtmlElementProperty("hgroup")
    main = HtmlElementProperty("main")
    nav = HtmlElementProperty("nav")
    section = HtmlElementProperty("section")
    #############
    # Headlines #
    #############
    h1 = HtmlElementProperty("h1")
    h2 = HtmlElementProperty("h2")
    h3 = HtmlElementProperty("h3")
    h4 = HtmlElementProperty("h4")
    h5 = HtmlElementProperty("h5")
    h6 = HtmlElementProperty("h6")
    ############
    # Grouping #
    ############
    blockquote = HtmlElementProperty("blockquote")
    dd = HtmlElementProperty("dd")
    div = HtmlElementProperty("div")
    dl = HtmlElementProperty("dl")
    dt = HtmlElementProperty("dt")
    figcaption = HtmlElementProperty("figcaption")
    figure = HtmlElementProperty("figure")
    hr = HtmlElementProperty("hr", close=False)
    li = HtmlElementProperty("li")
    ol = HtmlElementProperty("ol")
    p = HtmlElementProperty("p")
    pre = HtmlElementProperty("pre")
    ul = HtmlElementProperty("ul")
    ########
    # Text #
    ########
    a = HtmlElementProperty("a")
    abbr = HtmlElementProperty("abbr")
    b = HtmlElementProperty("b")
    bdi = HtmlElementProperty("bdi")
    bdo = HtmlElementProperty("bdo")
    br = HtmlElementProperty("br", close=False)
    cite = HtmlElementProperty("cite")
    code = HtmlElementProperty("code")
    dfn = HtmlElementProperty("dfn")
    em = HtmlElementProperty("em")
    i = HtmlElementProperty("i")
    kbd = HtmlElementProperty("kbd")
    mark = HtmlElementProperty("mark")
    q = HtmlElementProperty("q")
    rp = HtmlElementProperty("rp")
    rt = HtmlElementProperty("rt")
    ruby = HtmlElementProperty("ruby")
    s = HtmlElementProperty("s")
    samp = HtmlElementProperty("samp")
    small = HtmlElementProperty("small")
    span = HtmlElementProperty("span")
    strong = HtmlElementProperty("strong")
    sub = HtmlElementProperty("sub")
    sup = HtmlElementProperty("sup")
    time = HtmlElementProperty("time")
    u = HtmlElementProperty("u")
    var = HtmlElementProperty("var")
    wbr = HtmlElementProperty("wbr", close=False)
    #########
    # Edits #
    #########
    del_ = HtmlElementProperty("del")
    _del = HtmlElementProperty("del")
    ins = HtmlElementProperty("ins")
    ####################
    # Embedded Content #
    ####################
    area = HtmlElementProperty("area", close=False)
    audio = HtmlElementProperty("audio")
    canvas = HtmlElementProperty("canvas")
    embed = HtmlElementProperty("embed", close=False)
    iframe = HtmlElementProperty("iframe")
    img = HtmlElementProperty("img", close=False)
    map = HtmlElementProperty("map")
    object = HtmlElementProperty("object")
    param = HtmlElementProperty("param")
    source = HtmlElementProperty("source", close=False)
    track = HtmlElementProperty("track", close=False)
    video = HtmlElementProperty("video")
    #########
    # Table #
    #########
    caption = HtmlElementProperty("caption")
    col = HtmlElementProperty("col", close=False)
    colgroup = HtmlElementProperty("colgroup")
    table = HtmlElementProperty("table")
    tbody = HtmlElementProperty("tbody")
    tfoot = HtmlElementProperty("tfoot")
    thead = HtmlElementProperty("thead")
    td = HtmlElementProperty("td")
    th = HtmlElementProperty("th")
    tr = HtmlElementProperty("tr")
    ########
    # Form #
    ########
    button = HtmlElementProperty("button")
    datalist = HtmlElementProperty("datalist")
    fieldset = HtmlElementProperty("fieldset")
    form = HtmlElementProperty("form")
    keygen = HtmlElementProperty("keygen", close=False)
    input = HtmlElementProperty("input", close=False)
    label = HtmlElementProperty("label")
    legend = HtmlElementProperty("legend")
    meter = HtmlElementProperty("meter")
    optgroup = HtmlElementProperty("optgroup")
    option = HtmlElementProperty("option")
    output = HtmlElementProperty("output")
    progress = HtmlElementProperty("progress")
    select = HtmlElementProperty("select")
    textarea = HtmlElementProperty("textarea")
    ###############
    # Interactive #
    ###############
    command = HtmlElementProperty("command", close=False)
    details = HtmlElementProperty("details")
    font = HtmlElementProperty("font")
    menu = HtmlElementProperty("menu")
    summary = HtmlElementProperty("summary")

tag = Tag()
