from openerp import models, fields, api, exceptions, _
import pytz, datetime
from pytz import timezone
from datetime import datetime


class assistanceReportWizard(models.TransientModel):
	_name = 'assistance.set.period'
	date_start = fields.Date('Start Date')
	date_end = fields.Date('End Date')
	employee_id = fields.Many2one(
		comodel_name='hr.employee',
		string='Employee'
		)

	def print_report(self):
		assistance = self
		datas = {}
		if assistance.date_start >= assistance.date_end:
			raise exceptions.Warning(_('Warning!'),_('End date is %s must be greater then start date is %s') % (assistance.date_start,aassistance.date_end))
		#search employee services
		#assigned_ids = self.env["hr.assigned"].search_read([('employee','=',assistance.employee_id.id),
		assigned_ids = self.env["hr.assigned"].search([('employee','=',assistance.employee_id.id),
								('date','>=',assistance.date_start),
								('date','<=',assistance.date_end)],
								order='date asc')
		#UTC to local time
		local_tz = pytz.timezone('Europe/Madrid')
		#sustituir ora utc a hora local para el informe

		"""for service in assigned_ids:
			check_in = datetime.strptime(service['check_in'],"%Y-%m-%d %H:%M:%S")
			check_out = datetime.strptime(service['check_out'],"%Y-%m-%d %H:%M:%S")
			local_time_in = check_in.replace(tzinfo=pytz.utc).astimezone(local_tz)
			local_time_out = check_out.replace(tzinfo=pytz.utc).astimezone(local_tz)
			service['check_in']= local_time_in.strftime("%Y-%m-%d %H:%M:%S")
			service['check_out'] = local_time_out.strftime("%Y-%m-%d %H:%M:%S")"""

		if not assigned_ids:
			raise exceptions.Warning(_('Warning!'),_('The selected employee has no record in the selected period'))
		res= {'date_start':self.date_start,'date_end':self.date_end}
		d=[]
		for assigned in assigned_ids:
			turno = assigned.shift
			day = {
				"day":assigned.date[8:]+'/'+assigned.date[5:7],
	                        "entrada":turno.start,
        	                "salida":turno.end,
				"lunch":turno.lunch,
				"meal":turno.meal
			}

			if turno.lunch:
				day['lunch_start']=turno.lunch_start
				day['lunch_end']=turno.lunch_end
			if turno.meal:
        	                day['meal_start']=turno.meal_start
                	        day['meal_end']=turno.meal_end
			d.append(day)
		#raise exceptions.Warning(("TURNO",d))
		if assigned_ids:
			data = res
			datas = {
				'attendances': d,
				'form':data,
			}
		return self.env['report'].get_action(self,'ib_report_attendance_w.report_assistance_period_document', data=datas)


	@api.model
	def default_get(self, fields):
		res = super(assistanceReportWizard, self).default_get(fields)
		res.update({
			'date_start':self.env.context.get('start'),
			'date_end':self.env.context.get('end'),})
		return res
