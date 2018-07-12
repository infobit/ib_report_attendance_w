# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Listado de Fichadas',
    'version': '1.0',
    'category': 'hr',
    'description': """
Asistente generar informe fichadas por periodo
==================================
Este modulo crear un asistente para generar un informe de fichadas por periodo seleccionado
Solo muestra fichadas completas 'entrada y salida'
    """,
    'author': 'Infobit Informática',
    'website': 'http://www.infobit.es',
    'depends': ['hr_attendance'],
    'data': [
	'attendance_report.xml',
	'views/report_attendance_period.xml',
	'views/report_assistance_period.xml',
	'wizards/set_attendance_period_view.xml',
	'wizards/set_assistance_period_view.xml',
	'wizards/create_shift_assistance_view_2.xml',
	'views/hr_shift_view.xml',
	'views/hr_employee_view.xml',
	'views/hr_assigned_view.xml',
	'views/report_shift_period.xml',
	'wizards/set_shift_period_view.xml',
    ],
    'demo': [],
    'test': [],
    'css':['static/src/css/ib_report_activos.css'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:



