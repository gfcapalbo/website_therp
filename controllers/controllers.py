# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):
    @http.route('/academy/',auth='public',website=True)
    def index(self):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('website_therp.index',{
            'teachers': Teachers.search([]),
        })

    @http.route('/academy/<int:id>/',auth='public',website=True)
    def teacher(self,id):
        return '<h1>{} ({})</h1>'.format(id,type(id).__name__)
        # first bracket will accept id number, second name of the type (in this case int), all in header style
