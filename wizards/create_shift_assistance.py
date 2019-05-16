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
	def create_assigned_shift(self):
		#CREAR REGISTRO EN LOS DIAS SELECCIONADOS DE TURNO
		assigned_obj = self.env['hr.assigned']
		assigned = self
		datas = {}
		if assigned.date_start >= assigned.date_end:
			raise exceptions.Warning(_('Warning!'),_('End date is %s must be greater then start date is %s') % (attendance.date_start,attendance.date_end))

		fdesde = datetime.strptime(assigned.date_start, "%Y-%m-%d")
		fhasta = datetime.strptime(assigned.date_end, "%Y-%m-%d")

		day = timedelta(days=1)
		while fdesde <= fhasta:
			for employee in assigned.employee_id:
				assigned_obj.create({'employee': employee.id, 'shift': assigned.shift.id, 'date': fdesde})
			fdesde = fdesde + day

		"""#search employee services
		services_ids = self.env["hr.attendance"].search_read([('employee_id','=',attendance.employee_id.id),('check_in','>=',attendance.date_start),('check_out','<=',attendance.date_end)],order='check_in asc')
		#UTC to local time
		local_tz = pytz.timezone('Europe/Madrid')
		for service in services_ids:
			check_in = datetime.strptime(service['check_in'],"%Y-%m-%d %H:%M:%S")
			check_out = datetime.strptime(service['check_out'],"%Y-%m-%d %H:%M:%S")
			local_time_in = check_in.replace(tzinfo=pytz.utc).astimezone(local_tz)
			local_time_out = check_out.replace(tzinfo=pytz.utc).astimezone(local_tz)
			service['check_in']= local_time_in.strftime("%Y-%m-%d %H:%M:%S")
			service['check_out'] = local_time_out.strftime("%Y-%m-%d %H:%M:%S")

		if not services_ids:
			raise exceptions.Warning(_('Warning!'),_('The selected employee has no record in the selected period'))
		res= {'date_start':self.date_start,'date_end':self.date_end}
		if services_ids:
			data = res
			datas = {
				'attendances': services_ids,
				'form':data,
			}
		return self.env['report'].get_action(self,'ib_report_attendance_w.report_attendance_period_document', data=datas)"""

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
