# -*- coding: utf-8 -*-
##############################################################################
#
#    Perpul
#    Copyright (C) 2017 CodUP (<http://codup.com>).
#
##############################################################################

from flectra import api, fields, models, _


class asset_asset(models.Model):
    _inherit = 'asset.asset'

    position = fields.Char('Map')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:        