# -*- coding: utf-8 -*-
# Author: Guewen Baconnier
# Copyright 2013 Camptocamp SA
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# (http://www.serpentcs.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from flectra import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cancel_reason_id = fields.Many2one(
        'sale.order.cancel.reason',
        string="Reason for cancellation",
        readonly=True,
        ondelete="restrict")


class SaleOrderCancelReason(models.Model):
    _name = 'sale.order.cancel.reason'
    _description = 'Sale Order Cancel Reason'

    name = fields.Char('Reason', required=True, translate=True)
