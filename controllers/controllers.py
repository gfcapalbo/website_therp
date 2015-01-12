# -*- coding: utf-8 -*-
from openerp import http

class Academy(http.Controller):
    @http.route('/academy/',auth='public',website=True)
    def index(self):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('website_therp.index',{
            'teachers': Teachers.search([]),
        })

    @http.route('/academy/<model("academy.teachers"):teacher>/',auth='public',website=True)
    def teacher(self,teacher):
        return http.request.render('website_therp.biography',{
            'person': teacher
        })
    #
    # this time i'm accepting only objects of teacher type, defined in the model'


    @http.route('/academy/<model("academy.teachers"):teacher>/<model("academy.courses"):course>/',auth='public',website=True)
    def course(self,teacher,course):
        return http.request.render('website_therp.courseinfo',{
            'c': course
        })

