# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Avinash Nk(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from datetime import date
from flectra import models, fields, api


class SalonBookingBackend(models.Model):
    _name = 'salon.booking'

    name = fields.Char(string="Name")
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected')], default="draft")
    time = fields.Datetime(string="Date")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="E-Mail")
    services = fields.Many2many('salon.service', string="Services")
    chair_id = fields.Many2one('salon.chair', string="Chair")
    company_id = fields.Many2one('res.company', 'Company',
                                 default=lambda self: self.env['res.company'].browse(1))
    lang = fields.Many2one('res.lang', 'Language',
                           default=lambda self: self.env['res.lang'].browse(1))

    def all_salon_orders(self):
        if self.time:
            date_only = str(self.time)[0:10]
        else:
            date_only = date.today()
        all_salon_service_obj = self.env['salon.order'].search([('chair_id', '=', self.chair_id.id),
                                                                ('start_date_only', '=', date_only)])
        self.filtered_orders = [(6, 0, [x.id for x in all_salon_service_obj])]

    filtered_orders = fields.Many2many('salon.order', string="Salon Orders", compute="all_salon_orders")

    @api.multi
    def booking_approve(self):
        salon_order_obj = self.env['salon.order']
        salon_service_obj = self.env['salon.order.lines']
        order_data ={
            'customer_name': self.name,
            'chair_id': self.chair_id.id,
            'start_time': self.time,
            'date': date.today(),
            'stage_id': 1,
            'booking_identifier': True,
        }
        order = salon_order_obj.create(order_data)
        for records in self.services:
            service_data = {
                'service_id': records.id,
                'time_taken': records.time_taken,
                'price': records.price,
                'price_subtotal': records.price,
                'salon_order': order.id,
            }
            salon_service_obj.create(service_data)
        template = self.env.ref('salon_management.salon_email_template_approved')
        self.env['mail.template'].browse(template.id).send_mail(self.id)
        self.state = "approved"

    @api.multi
    def booking_reject(self):
        template = self.env.ref('salon_management.salon_email_template_rejected')
        self.env['mail.template'].browse(template.id).send_mail(self.id)
        self.state = "rejected"

