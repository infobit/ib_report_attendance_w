# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class shift(models.Model):
	_name = 'hr.shift'
	
	name = fields.Char('Name')
	start = fields.Float('Start Date')
	end = fields.Float('End Date')

	lunch = fields.Boolean()
	lunch_start = fields.Float('Lunch start date')
	lunch_end = fields.Float('Lunch end date')

	meal = fields.Boolean()
	meal_start = fields.Float('meal start')
	meal_end = fields.Float('meal end')

	sequence= fields.Integer('sequence')

	monday = fields.Boolean('Monday',default=True)
	tuesday = fields.Boolean('Tuesday',default=True)
	wednesday = fields.Boolean('Wednesday',default=True)
	thursday = fields.Boolean('Thursday',default=True)
	friday = fields.Boolean('Friday',default=True)
	saturday = fields.Boolean('Saturday',default=True)
	sunday = fields.Boolean('Sunday',default=True)

	visible = fields.Boolean(default=True)

class assigned(models.Model):
	_name = 'hr.assigned'

	date = fields.Date()
	shift = fields.Many2one('hr.shift','Shift')
	employee = fields.Many2one('hr.employee','Employee')
	notes = fields.Text('Notes')
	visible = fields.Boolean(related="shift.visible",store=True)
