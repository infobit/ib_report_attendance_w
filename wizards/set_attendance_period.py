from openerp import models, fields, api, exceptions, _

class attendanceReportWizard(models.TransientModel):
	_name = 'attendance.set.period'
	#_inherit = 'hr.attendance'
	date_start = fields.Date('Start Date')
	date_end = fields.Date('End Date')
	employee_id = fields.Many2one(
		comodel_name='hr.employee',
		string='Employee'
		)

	def print_report(self,cr,uid,ids,context=None):
	    attendance = self.browse(cr,uid,ids,context=context)
	    datas = {}
            if attendance.date_start >= attendance.date_end:
	    	raise exceptions.Warning(_('Warning!'),_('End date is %s must be greater then start date is %s') % (attendance.date_start,attendance.date_end))
	    #search employee services
	    services_ids = self.pool.get("hr.attendance").search_read(cr,uid,[('employee_id','=',attendance.employee_id.id),('name','>=',attendance.date_start),('name','<=',attendance.date_end)],context=context)
	    services_ids.reverse() 
	    #raise exceptions.Warning(services_ids[0]['display_name'])
	    if not services_ids:
		raise exceptions.Warning(_('Warning!'),_('The selected employee has no record in the selected period'))
	    #res= {'date_start':activo.date_start,'date_end':activo.date_end}
            res = self.read(cr, uid, ids)[0]
	    #raise exceptions.Warning(res)
	    if services_ids:
	            data = res
	            datas = {
		            'attendances': services_ids,
#		            'model': 'account.report.active', # wizard model name
			    'form':data,
#		            'context':context
	            }
#	    raise exceptions.Warning(datas['form'][0]['date_start'])
	    #raise exceptions.Warning(datas)
	    
	    return self.pool['report'].get_action(cr, uid, [],'ib_report_attendance_w.report_attendance_period_document', data=datas, context=context)

#            return {
#                   'type': 'ir.actions.report.xml',
#                   'report_name': 'ib_report_activos.report_activo_grupo_document',#module name.report template name
#                   'data': datas,
#               }	   


	@api.model
	def default_get(self, fields):
		res = super(attendanceReportWizard, self).default_get(fields)
		res.update({
			'date_start':self.env.context.get('start'),
			'date_end':self.env.context.get('end'),})
		return res
