# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):
    @http.route('/academy/',auth='public',website=True)
    def index(self):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('website_therp.index',{
            'teachers': Teachers.search([]),
        })
