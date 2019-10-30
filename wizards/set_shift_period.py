# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
import pytz, datetime
from pytz import timezone
from datetime import datetime


class shiftReportWizard(models.TransientModel):
	_name = 'shift.set.period'
	date_start = fields.Date('Start Date')
	date_end = fields.Date('End Date')

	@api.multi
	def print_report(self):
		assistance = self
		datas = {}
		if assistance.date_start > assistance.date_end:
			raise exceptions.Warning(_('Warning!'),_('End date is %s must be greater then start date is %s') % (assistance.date_start,aassistance.date_end))
	    	#Buscar asginaciones de empleados
	    	#search employee services
	    	#assigned_ids = self.env["hr.assigned"].search_read([('employee','=',assistance.employee_id.id),
		shift_ids = self.env['hr.shift'].search([],order='sequence');
	    	#if not shift_ids:raise exceptions.Warning(_('Warning!'),_('No created shift, create shifts'))
		d = []
		for shift in shift_ids:
			hora_ini = '%s:%02d' %(str(shift.start).split('.')[0], int(round(float(str('%.2f' % shift.start).split('.')[1])/100*60)))
			hora_fin = '%s:%02d' %(str(shift.end).split('.')[0], int(round(float(str('%.2f' % shift.end).split('.')[1])/100*60)))
			hora_al_ini = '%s:%02d' % (str(shift.lunch_start).split('.')[0], int(round(float(str('%.2f' % shift.lunch_start).split('.')[1])/100*60)))
			hora_al_fin = '%s:%02d' %(str(shift.lunch_end).split('.')[0], int(round(float(str('%.2f' % shift.lunch_end).split('.')[1])/100*60)))
			hora_co_ini = '%s:%02d' %(str(shift.meal_start).split('.')[0], int(round(float(str('%.2f' % shift.meal_start).split('.')[1])/100*60)))
			hora_co_fin = '%s:%02d' %(str(shift.meal_end).split('.')[0], int(round(float(str('%.2f' % shift.meal_end).split('.')[1])/100*60)))
			name = shift.name or ""
			shift_name = name+" "+hora_ini

			if(shift.lunch):
				shift_name = shift_name+" - "+hora_al_ini+" // "+hora_al_fin
			if(shift.meal):
				shift_name = shift_name+" - "+hora_co_ini+" // "+hora_co_fin
			shift_name = shift_name+" - "+hora_fin

			assigned_ids = self.env["hr.assigned"].search([
							('shift','=',shift.id),
							('date','>=',assistance.date_start),
						   	('date','<=',assistance.date_end)],order="date,employee asc")

			start = self.date_start
			end = self.date_end
			employees_day = []
			employees=[]
			date = ""
			first_date = start
			for assigned in assigned_ids:
				date = assigned.date
	                	#raise exceptions.Warning((first_date,date))
				if(first_date != date):
					employees_day.append((first_date,employees))
					first_date = date
	                		#raise exceptions.Warning(employees_day)
					employees=[]
				employees.append(assigned.employee.name)
			if employees:
				employees_day.append((first_date,employees))
			#employees_day.append(employees)
			d.append((shift_name,employees_day))
		datas = {
			'shift': d,
			'model': self._name,
            	}
		return self.env['report'].get_action(self,'ib_report_attendance_w.report_shift_period_document', data=datas)
		#return self.env.ref('ib_report_attendance_w.custom_report_shift_period').report_action(self, data=datas)

	@api.model
	def default_get(self, fields):
		res = super(shiftReportWizard, self).default_get(fields)
		res.update({
			'date_start':self.env.context.get('start'),
			'date_end':self.env.context.get('end'),})
		return res
