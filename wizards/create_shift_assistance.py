from openerp import models, fields, api, exceptions, _
import pytz, datetime
from pytz import timezone
from datetime import datetime,timedelta


class assistanceCreateShift(models.TransientModel):
	_name = 'hr.assistance.set.shift'
	date_start = fields.Date('Start Date')
	date_end = fields.Date('End Date')
	employee_id = fields.Many2many(
		comodel_name='hr.employee',
		string='Employee'
	)
	shift = fields.Many2one('hr.shift','Shift')

	@api.multi
	def create_assigned_shift(self):
		#CREAR REGISTRO EN LOS DIAS SELECCIONADOS DE TURNO
		assigned_obj = self.env['hr.assigned']
		assigned = self
		datas = {}
		week   = [
			assigned.shift.monday, 
			assigned.shift.tuesday,
			assigned.shift.wednesday,
			assigned.shift.thursday,
			assigned.shift.friday,
			assigned.shift.saturday,
			assigned.shift.sunday
			]
		if assigned.date_start > assigned.date_end:
			raise exceptions.Warning(_('Warning!'),_('End date is %s must be greater then start date is %s') % (attendance.date_start,attendance.date_end))

		fdesde = datetime.strptime(assigned.date_start, "%Y-%m-%d")
		fhasta = datetime.strptime(assigned.date_end, "%Y-%m-%d")

		day = timedelta(days=1)
		while fdesde <= fhasta:
			if week[fdesde.weekday()]:
				for employee in assigned.employee_id:
					assigned_obj.create({'employee': employee.id, 'shift': assigned.shift.id, 'date': fdesde})
			fdesde = fdesde + day

	@api.model
	def default_get(self, fields):
		res = super(assistanceCreateShift, self).default_get(fields)
		res.update({
			'date_start':self.env.context.get('start'),
			'date_end':self.env.context.get('end'),
			'shift':self.env.context.get('shift'),
			'employee_id':self.env.context.get('employee_id')
			})
		return res
