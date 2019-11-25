# -*- encoding: utf-8 -*-
from openerp import api, models, fields, _

class hr_employee(models.Model):
	_name = "hr.employee"
	_inherit = "hr.employee"

	holiday_old = fields.Integer("Old Holiday's")
	holiday_new = fields.Integer("New Holiday's")
	#assigned = fields.One2many('hr.assigned','employee')
