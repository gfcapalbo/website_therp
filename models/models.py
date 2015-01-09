from openerp import fields
from openerp import models

class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char()

