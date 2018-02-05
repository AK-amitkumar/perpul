# -*- coding: utf-8 -*-
##############################################################################
#
#    Perpul
#    Copyright (C) 2017 CodUP (<http://codup.com>).
#
##############################################################################

from flectra import models
from flectra.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def webclient_rendering_context(self):
        rendering_context = super(Http, self).webclient_rendering_context()
        rendering_context['google_maps_api_key'] = request.env['ir.config_parameter'].sudo().get_param('google_maps_api_key')
        return rendering_context

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:        