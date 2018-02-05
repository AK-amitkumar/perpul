import json
import logging
from werkzeug.exceptions import Forbidden

from flectra import http, tools, _
from flectra.http import request
from flectra.addons.base.ir.ir_qweb.fields import nl2br
from flectra.addons.website.models.website import slug
from flectra.addons.website.controllers.main import QueryURL
from flectra.exceptions import ValidationError
from flectra.addons.website_form.controllers.main import WebsiteForm

from flectra.addons.website_sale.controllers.main import WebsiteSale as org

_logger = logging.getLogger(__name__)

class WebsiteSale(org):
    def values_preprocess(self, order, mode, values):
        if 'vat' in values:
            icp = request.env['ir.config_parameter']
            demand_vat = icp.get_param('bc_confirm_and_send_so_require_vat')
            if not demand_vat:
                _logger.info('bc_confirm_and_send_so values_preprocess NOT adding VAT prefix')
            else:
                _logger.info('bc_confirm_and_send_so values_preprocess adding VAT prefix. is VAT even required? %s', demand_vat)
                vat = values['vat']
                prefix = vat[:2]
                if not prefix.isalpha():
                    values['vat'] = 'NO' + vat

        return super(WebsiteSale, self).values_preprocess(order, mode, values)

    def checkout_form_validate(self, mode, all_form_values, data):
        error = super(WebsiteSale, self).checkout_form_validate(mode, all_form_values, data)
        icp = request.env['ir.config_parameter']
        demand_vat = icp.get_param('bc_confirm_and_send_so_require_vat')
        _logger.info('Controller Is VAT number required by bc_confirm_and_send FORM? %s ( bc_confirm_and_send_so_require_vat )',
                     demand_vat)

        if demand_vat and not data.get('vat'):
            _logger.info('We demand VAT')
            error['vat'] = 'missing'

        return error


