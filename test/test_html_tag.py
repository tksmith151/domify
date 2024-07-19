import unittest

from src.pydomify import tag

class TestHtmlTag(unittest.TestCase):

    ########
    # Root #
    ########

    def test_doctype(self):
        self.assertEqual(tag.doctype.render(), '<!DOCTYPE>')

    def test_html(self):
        self.assertEqual(tag.html.render(), '<html></html>')

    ############
    # Metadata #
    ############

    def test_base(self):
        self.assertEqual(tag.base.render(), '<base>')
        
    def test_head(self):
        self.assertEqual(tag.head.render(), '<head></head>')

    def test_link(self):
        self.assertEqual(tag.link.render(), '<link>')

    def test_meta(self):
        self.assertEqual(tag.meta.render(), '<meta>')

    def test_noscript(self):
        self.assertEqual(tag.noscript.render(), '<noscript></noscript>')

    def test_script(self):
        self.assertEqual(tag.script.render(), '<script></script>')

    def test_style(self):
        self.assertEqual(tag.style.render(), '<style></style>')

    def test_title(self):
        self.assertEqual(tag.title.render(), '<title></title>')

    ############
    # Sections #
    ############

    def test_address(self):
        self.assertEqual(tag.address.render(), '<address></address>')
    
    def test_article(self):
        self.assertEqual(tag.article.render(), '<article></article>')

    def test_aside(self):
        self.assertEqual(tag.aside.render(), '<aside></aside>')

    def test_body(self):
        self.assertEqual(tag.body.render(), '<body></body>')

    def test_footer(self):
        self.assertEqual(tag.footer.render(), '<footer></footer>')
    
    def test_header(self):
        self.assertEqual(tag.header.render(), '<header></header>')

    def test_hgroup(self):
        self.assertEqual(tag.hgroup.render(), '<hgroup></hgroup>')

    def test_main(self):
        self.assertEqual(tag.main.render(), '<main></main>')

    def test_nav(self):
        self.assertEqual(tag.nav.render(), '<nav></nav>')
    
    def test_section(self):
        self.assertEqual(tag.section.render(), '<section></section>')

    #############
    # Headlines #
    #############

    def test_h1(self):
        self.assertEqual(tag.h1.render(), '<h1></h1>')
    
    def test_h2(self):
        self.assertEqual(tag.h2.render(), '<h2></h2>')

    def test_h3(self):
        self.assertEqual(tag.h3.render(), '<h3></h3>')

    def test_h4(self):
        self.assertEqual(tag.h4.render(), '<h4></h4>')

    def test_h5(self):
        self.assertEqual(tag.h5.render(), '<h5></h5>')

    def test_h6(self):
        self.assertEqual(tag.h6.render(), '<h6></h6>')

    ############
    # Grouping #
    ############

    def test_blockquote(self):
        self.assertEqual(tag.blockquote.render(), '<blockquote></blockquote>')

    def test_dd(self):
        self.assertEqual(tag.dd.render(), '<dd></dd>')
    
    def test_div(self):
        self.assertEqual(tag.div.render(), '<div></div>')

    def test_dl(self):
        self.assertEqual(tag.dl.render(), '<dl></dl>')

    def test_dt(self):
        self.assertEqual(tag.dt.render(), '<dt></dt>')

    def test_figcaption(self):
        self.assertEqual(tag.figcaption.render(), '<figcaption></figcaption>')
    
    def test_figure(self):
        self.assertEqual(tag.figure.render(), '<figure></figure>')

    def test_hr(self):
        self.assertEqual(tag.hr.render(), '<hr>')

    def test_li(self):
        self.assertEqual(tag.li.render(), '<li></li>')

    def test_ol(self):
        self.assertEqual(tag.ol.render(), '<ol></ol>')

    def test_p(self):
        self.assertEqual(tag.p.render(), '<p></p>')
    
    def test_pre(self):
        self.assertEqual(tag.pre.render(), '<pre></pre>')

    def test_ul(self):
        self.assertEqual(tag.ul.render(), '<ul></ul>')

    ########
    # Text #
    ########

    def test_a(self):
        self.assertEqual(tag.a.render(), '<a></a>')

    def test_abbr(self):
        self.assertEqual(tag.abbr.render(), '<abbr></abbr>')
    
    def test_b(self):
        self.assertEqual(tag.b.render(), '<b></b>')

    def test_bdi(self):
        self.assertEqual(tag.bdi.render(), '<bdi></bdi>')

    def test_bdo(self):
        self.assertEqual(tag.bdo.render(), '<bdo></bdo>')

    def test_br(self):
        self.assertEqual(tag.br.render(), '<br>')

    def test_cite(self):
        self.assertEqual(tag.cite.render(), '<cite></cite>')
    
    def test_code(self):
        self.assertEqual(tag.code.render(), '<code></code>')

    def test_dfn(self):
        self.assertEqual(tag.dfn.render(), '<dfn></dfn>')

    def test_em(self):
        self.assertEqual(tag.em.render(), '<em></em>')

    def test_i(self):
        self.assertEqual(tag.i.render(), '<i></i>')
    
    def test_kbd(self):
        self.assertEqual(tag.kbd.render(), '<kbd></kbd>')

    def test_mark(self):
        self.assertEqual(tag.mark.render(), '<mark></mark>')

    def test_q(self):
        self.assertEqual(tag.q.render(), '<q></q>')

    def test_rp(self):
        self.assertEqual(tag.rp.render(), '<rp></rp>')

    def test_rt(self):
        self.assertEqual(tag.rt.render(), '<rt></rt>')
    
    def test_ruby(self):
        self.assertEqual(tag.ruby.render(), '<ruby></ruby>')

    def test_s(self):
        self.assertEqual(tag.s.render(), '<s></s>')

    def test_samp(self):
        self.assertEqual(tag.samp.render(), '<samp></samp>')

    def test_small(self):
        self.assertEqual(tag.small.render(), '<small></small>')
    
    def test_span(self):
        self.assertEqual(tag.span.render(), '<span></span>')

    def test_strong(self):
        self.assertEqual(tag.strong.render(), '<strong></strong>')

    def test_sub(self):
        self.assertEqual(tag.sub.render(), '<sub></sub>')

    def test_sup(self):
        self.assertEqual(tag.sup.render(), '<sup></sup>')

    def test_time(self):
        self.assertEqual(tag.time.render(), '<time></time>')
    
    def test_u(self):
        self.assertEqual(tag.u.render(), '<u></u>')

    def test_var(self):
        self.assertEqual(tag.var.render(), '<var></var>')

    def test_wbr(self):
        self.assertEqual(tag.wbr.render(), '<wbr>')

    #########
    # Edits #
    #########

    def test_del_(self):
        self.assertEqual(tag.del_.render(), '<del></del>')
    
    def test__del(self):
        self.assertEqual(tag._del.render(), '<del></del>')

    def test_ins(self):
        self.assertEqual(tag.ins.render(), '<ins></ins>')

    ####################
    # Embedded Content #
    ####################

    def test_area(self):
        self.assertEqual(tag.area.render(), '<area>')

    def test_audio(self):
        self.assertEqual(tag.audio.render(), '<audio></audio>')

    def test_canvas(self):
        self.assertEqual(tag.canvas.render(), '<canvas></canvas>')
    
    def test_embed(self):
        self.assertEqual(tag.embed.render(), '<embed>')

    def test_iframe(self):
        self.assertEqual(tag.iframe.render(), '<iframe></iframe>')

    def test_img(self):
        self.assertEqual(tag.img.render(), '<img>')

    def test_map(self):
        self.assertEqual(tag.map.render(), '<map></map>')
    
    def test_object(self):
        self.assertEqual(tag.object.render(), '<object></object>')

    def test_param(self):
        self.assertEqual(tag.param.render(), '<param></param>')

    def test_source(self):
        self.assertEqual(tag.source.render(), '<source>')

    def test_track(self):
        self.assertEqual(tag.track.render(), '<track>')

    def test_video(self):
        self.assertEqual(tag.video.render(), '<video></video>')
    
    #########
    # Table #
    #########

    def test_caption(self):
        self.assertEqual(tag.caption.render(), '<caption></caption>')

    def test_col(self):
        self.assertEqual(tag.col.render(), '<col>')

    def test_colgroup(self):
        self.assertEqual(tag.colgroup.render(), '<colgroup></colgroup>')

    def test_table(self):
        self.assertEqual(tag.table.render(), '<table></table>')
    
    def test_tbody(self):
        self.assertEqual(tag.tbody.render(), '<tbody></tbody>')

    def test_tfoot(self):
        self.assertEqual(tag.tfoot.render(), '<tfoot></tfoot>')

    def test_thead(self):
        self.assertEqual(tag.thead.render(), '<thead></thead>')

    def test_td(self):
        self.assertEqual(tag.td.render(), '<td></td>')

    def test_th(self):
        self.assertEqual(tag.th.render(), '<th></th>')
    
    def test_tr(self):
        self.assertEqual(tag.tr.render(), '<tr></tr>')

    ########
    # Form #
    ########

    def test_button(self):
        self.assertEqual(tag.button.render(), '<button></button>')

    def test_datalist(self):
        self.assertEqual(tag.datalist.render(), '<datalist></datalist>')

    def test_fieldset(self):
        self.assertEqual(tag.fieldset.render(), '<fieldset></fieldset>')
    
    def test_form(self):
        self.assertEqual(tag.form.render(), '<form></form>')

    def test_keygen(self):
        self.assertEqual(tag.keygen.render(), '<keygen>')

    def test_input(self):
        self.assertEqual(tag.input.render(), '<input>')

    def test_label(self):
        self.assertEqual(tag.label.render(), '<label></label>')

    def test_legend(self):
        self.assertEqual(tag.legend.render(), '<legend></legend>')
    
    def test_meter(self):
        self.assertEqual(tag.meter.render(), '<meter></meter>')

    def test_optgroup(self):
        self.assertEqual(tag.optgroup.render(), '<optgroup></optgroup>')

    def test_option(self):
        self.assertEqual(tag.option.render(), '<option></option>')

    def test_output(self):
        self.assertEqual(tag.output.render(), '<output></output>')
    
    def test_progress(self):
        self.assertEqual(tag.progress.render(), '<progress></progress>')

    def test_select(self):
        self.assertEqual(tag.select.render(), '<select></select>')

    def test_textarea(self):
        self.assertEqual(tag.textarea.render(), '<textarea></textarea>')

    ###############
    # Interactive #
    ###############

    def test_command(self):
        self.assertEqual(tag.command.render(), '<command>')

    def test_details(self):
        self.assertEqual(tag.details.render(), '<details></details>')
    
    def test_font(self):
        self.assertEqual(tag.font.render(), '<font></font>')

    def test_menu(self):
        self.assertEqual(tag.menu.render(), '<menu></menu>')

    def test_summary(self):
        self.assertEqual(tag.summary.render(), '<summary></summary>')

if __name__ == '__main__':
    unittest.main()