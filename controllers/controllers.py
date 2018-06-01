# -*- coding: utf-8 -*-
from odoo import http

# class Customize(http.Controller):
#     @http.route('/customize/customize/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customize/customize/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customize.listing', {
#             'root': '/customize/customize',
#             'objects': http.request.env['customize.customize'].search([]),
#         })

#     @http.route('/customize/customize/objects/<model("customize.customize"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customize.object', {
#             'object': obj
#         })