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
    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True)
    def confirm_order(self, **post):
        # Copied from the same method in website_sale
        order = request.website.sale_get_order()

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        order.onchange_partner_shipping_id()
        order.order_line._compute_tax_id()
        request.session['sale_last_order_id'] = order.id
        request.website.sale_get_order(update_pricelist=True)
        icp = request.env['ir.config_parameter']
        which_categ = icp.get_param('bc_extra_step_conditional_categ')
        pcat = request.env['product.public.category'].search([('name', '=', which_categ)])
        if not pcat:
            raise ValidationError('No category called %s is defined' % which_categ)

        categories = [x.product_id.public_categ_ids for x in order.order_line]
        _logger.info('Confirm order, categories %s', categories)

        extra_step = request.env.ref('website_sale.extra_info_option')
        if pcat in categories and extra_step.active:
            return request.redirect("/shop/extra_info")

        return request.redirect("/shop/payment")
