# -*- encoding: utf-8 -*-
from openerp import api, models, fields, _
from zklib import *

class hr_employee(models.Model):
	_name = "hr.employee"
	_inherit = "hr.employee"

	assigned = fields.One2many('hr.assigned','employee')
