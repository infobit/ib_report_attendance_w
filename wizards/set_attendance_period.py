from openerp import models, fields, api, exceptions, _
import pytz, datetime
from pytz import timezone
from datetime import datetime


class attendanceReportWizard(models.TransientModel):
	_name = 'attendance.set.period'
	date_start = fields.Date('Start Date')
	date_end = fields.Date('End Date')
	employee_id = fields.Many2one(
		comodel_name='hr.employee',
		string='Employee'
		)
	def print_report(self):
		attendance = self
		datas = {}
		if attendance.date_start >= attendance.date_end:
			raise exceptions.Warning(_('Warning!'),_('End date is %s must be greater then start date is %s') % (attendance.date_start,attendance.date_end))
		#search employee services
		services_ids = self.env["hr.attendance"].search_read([
					('employee_id','=',attendance.employee_id.id),
					('check_in','>=',attendance.date_start),
					('check_out','<=',attendance.date_end)],order='check_in asc')
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
		return self.env['report'].get_action(self,'ib_report_attendance_w.report_attendance_period_document', data=datas)

	@api.model
	def default_get(self, fields):
		res = super(attendanceReportWizard, self).default_get(fields)
		res.update({
			'date_start':self.env.context.get('start'),
			'date_end':self.env.context.get('end'),})
		return res
