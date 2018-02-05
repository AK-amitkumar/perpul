# -*- coding: utf-8 -*-

from flectra import fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    user_id = fields.Many2one('res.users', string="Salesperson")
