# -*- coding: utf-8 -*-
# Copyright 2016-TODAY Serpent Consulting Services Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    over_credit = fields.Boolean('Allow Over Credit?')
