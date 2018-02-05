from flectra import http
from flectra.http import request
from flectra.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSeoSuite(WebsiteSale):
    
    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res=super(WebsiteSeoSuite, self).shop(page, category, search, ppg, **post)
        if category :
            category = request.env['product.public.category'].browse(int(category))
            attrib_list = request.httprequest.args.getlist('attrib')
            products=res.qcontext['products']
            if attrib_list :
                value_dict_category=category.sudo().get_seo_template_value_for_attribute(products)
                if value_dict_category :
                    res.qcontext.update(value_dict_category)
            else :
                value_dict_category=category.sudo().get_seo_template_value_for_category(products)
                if value_dict_category :
                    res.qcontext.update(value_dict_category)
        return res

    
    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        res=super(WebsiteSeoSuite, self).product(product, category, search, **kwargs)
        # apply template on product page
        if category :
            category=request.env['product.public.category'].browse(int(category))
        value_dict=product.sudo().get_value_of_field(category)
        if value_dict :
            res.qcontext.update(value_dict)
        return res
    
          