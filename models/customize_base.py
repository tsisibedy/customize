# -*- coding: utf-8 -*-

import sys, os
import re
import werkzeug
from odoo import models, fields, api



class Customize(models.Model):
    _name = 'customize.base'

    name = fields.Char(string='Theme name')
    o_skew_gradient_primary = fields.Char(string='Main color primary(hexadecimal color)')
    o_skew_gradient_second = fields.Char(string='Main color second(hexadecimal color)')
    odoo_brand_primary = fields.Char(string='Primary color(hexadecimal color)')
    brand_optional = fields.Char('Optional color(hexadecimal color)')

    def open_file_and_edit(self,file_name,text_search,text_replace):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        file_path = str(dir_path).replace('customize\models','customize\static\src\less\\%s'%file_name)
        replace_file = open(file_path, 'r+')
        for line in replace_file:
            if text_search in line:
                replace_text = line
                file_app_switcher_read = open(file_path).read()
                file_app_switcher_read = file_app_switcher_read.replace(replace_text, text_replace)

                file_app_switcher_write = open(file_path, 'w')
                file_app_switcher_write.write(file_app_switcher_read)
                file_app_switcher_write.close()

    def active_this_theme(self):
        file_name_skew_gradient = 'app_switcher.less'
        file_name_variables = 'variables.less'
        text_search_skew_gradient = '.o-skew-gradient'
        text_search_brand_primary = '@odoo-brand-primary:'
        text_search_brand_optional = '@odoo-brand-optional:'
        for record in self:
            text_replace_skew_gradient = '\t.o-skew-gradient(%s, %s);\n' % (record.o_skew_gradient_primary, record.o_skew_gradient_second)
            self.open_file_and_edit(file_name_skew_gradient,text_search_skew_gradient,text_replace_skew_gradient)
            text_replace_brand_primary = '@odoo-brand-primary: %s;\n' % record.odoo_brand_primary
            self.open_file_and_edit(file_name_variables,text_search_brand_primary,text_replace_brand_primary)
            text_replace_brand_optional = '@odoo-brand-optional: %s;\n' % record.brand_optional
            self.open_file_and_edit(file_name_variables,text_search_brand_optional,text_replace_brand_optional)








