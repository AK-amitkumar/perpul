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
		# TODO Make this dynamic
		_logger.info('Default Country')
		rc = request.env['res.country']
		country = rc.browse(167)
		assert country.code == 'NO'
		if 'country_id' not in values or not values['country_id']:
			values['country_id'] = country.id
		if 'vat' in values:
			if len(values['vat']) > 2 and not values['vat'][:2].isalpha():
				values['vat'] = 'NO' + values['vat']

		_logger.info('Default Country is now set %s', values)
		return super(WebsiteSale, self).values_preprocess(order, mode, values)
