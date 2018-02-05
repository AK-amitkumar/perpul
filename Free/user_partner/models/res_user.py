# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from flectra import models, fields, api, _


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        user = super(ResUsers, self).create(vals)
        user.partner_id.customer = False
        return user        