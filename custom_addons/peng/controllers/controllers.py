# -*- coding: utf-8 -*-
from odoo import http


class Peng(http.Controller):
    @http.route('/peng/peng', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/peng/peng/objects', auth='public')
    def list(self, **kw):
        return http.request.render('peng.listing', {
            'root': '/peng/peng',
            'objects': http.request.env['peng.peng'].search([]),
        })

    @http.route('/peng/peng/objects/<model("peng.peng"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('peng.object', {
            'object': obj
        })

