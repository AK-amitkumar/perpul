# -*- coding: utf-8 -*-
##############################################################################
#
#    Perpul
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from flectra import api, fields, models

class Users(models.Model):
    _inherit = 'res.users'

    print_facsimile = fields.Boolean('Print Facsimile', related='company_id.print_facsimile')
    facsimile = fields.Binary("Facsimile")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:        