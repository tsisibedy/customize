# -*- coding: utf-8 -*-
{
    'name': "Customize",
    'icon': '/customize/static/src/img/customize.png',
    'summary': "",

    'description': "Module to customize odoo color",

    'author': "Razafimiandrisoa Noarison Léonce",
    'category': 'Uncategorized',
    'version': '0.2',
    'depends': ['base', 'web', 'web_enterprise'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/srm_base_data.xml',
        'views/customize_base.xml',
        'views/templates.xml',
        'data/odoo_native_theme.sql',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/widget.xml',
    ],
}
