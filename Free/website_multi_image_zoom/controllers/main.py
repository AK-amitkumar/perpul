# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from flectra import http
from flectra.http import request
from flectra.addons.website_sale.controllers import main


class WebsiteSale(main.WebsiteSale):
    @http.route(['/get_variant_images'], type='json', auth='public',
                methods=['POST'])
    def get_variant_images(self, **post):
        variant_images = request.env['product.image'].sudo(). \
            search([('product_variant_id', '=', int(post.get('product_id')))])
        images = [img.id for img in variant_images]
        return {'product_rec': images}
