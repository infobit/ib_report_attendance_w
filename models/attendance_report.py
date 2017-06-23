# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class Attendance(models.Model):
	_inherit = 'hr.attendance'
	_name = 'attendance.report.period'

	start = fields.Date('Start Date')
	end = fields.Date('End Date')
	employee = fields.Many2one(
                comodel_name='hr.employee',
                string='Employee'
                )
	duration = fields.Float('duration')
