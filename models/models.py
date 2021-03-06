from openerp import fields
from openerp import models

class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses','teacher_id',string="Courses")

class Courses(models.Model):
    _name = 'academy.courses'
    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers',string="Teacher")
    extra_info = fields.Html()

