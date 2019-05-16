# -*- coding: utf-8 -*-

from datetime import datetime, date, time, timedelta
from openerp import models,api,exceptions
from openerp.report import report_sxw
import math

class assistance_period_parser(report_sxw.rml_parse):

	def __init__(self, cr, uid, name, context):
		super(assistance_period_parser, self).__init__(cr, uid, name, context=context)
	        self.localcontext.update({
	            'hello': self._hello,
	            'random': self._random,
		    'get_year': self._get_year,
		    'compare_date':self._compare_date,
		    'compare_date_ini':self._compare_date_ini,
		    'compare_year':self._compare_year
		})


	def _random(self,day,hora):
		#return "hola"
		minutos = math.sin(int(day[:2])*int(day[3:])+hora)/10
		#nhora = float(str(minutos)[:2])/(100*int(str(minutos)[:1]))
		return minutos+hora

	def _hello(self):
	 	return "Hello World!"
	
	def _get_year(self,date):
		year=date[:4]
		#raise exceptions.Warning(year)
		return int(year) 
	def _compare_date(self,date1,date2):
		#raise exceptions.Warning(date1,date2)
		#activo = date(int(date1[6:]),int(date1[3:5]),int(date1[:2]))
		#final = date(int(date2[6:]),int(date2[3:5]),int(date2[:2]))
		activo = int(date1[6:])
		final = int(date2[6:])
		return activo<=final
	def _compare_date_ini(self,date1,date2):
		#raise exceptions.Warning(date1,date2)
		#activo = date(int(date1[6:]),int(date1[3:5]),int(date1[:2]))
		#inicio = date(int(date2[6:]),int(date2[3:5]),int(date2[:2]))
		activo = int(date1[6:])
		#inicio = int(date2[6:])
		inicio = int(date2)
		return activo<=inicio
	def _compare_year(self,date1,year):
		#raise exceptions.Warning(date1,date2)
		#activo = date(int(date1[6:]),int(date1[3:5]),int(date1[:2]))
		#inicio = date(int(date2[6:]),int(date2[3:5]),int(date2[:2]))
		activo = int(date1[6:])
		a = int(year)
		return activo==a

class report_period_parser(models.AbstractModel):
    _name = 'report.ib_report_attendance_w.report_assistance_period_document'
    _inherit = 'report.abstract_report'
    _template = 'ib_report_attendance_w.report_assistance_period_document'
    _wrapped_report_class =  assistance_period_parser


