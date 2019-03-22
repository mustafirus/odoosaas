# -*- coding: utf-8 -*-
from odoo import http

# class Odoosaas(http.Controller):
#     @http.route('/odoosaas/odoosaas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoosaas/odoosaas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoosaas.listing', {
#             'root': '/odoosaas/odoosaas',
#             'objects': http.request.env['odoosaas.odoosaas'].search([]),
#         })

#     @http.route('/odoosaas/odoosaas/objects/<model("odoosaas.odoosaas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoosaas.object', {
#             'object': obj
#         })