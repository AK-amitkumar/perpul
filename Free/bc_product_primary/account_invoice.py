

from openerp import api, fields, models, _,exceptions
import logging

_logger = logging.getLogger(__name__)


class ProductCategory(models.Model):
    _inherit = "product.category"

    def contains(self, product_id):
        self.ensure_one()
        category = product_id.categ_id
        if category == self:
            return True

        while category.parent_id:
            parent = category.parent_id
            if parent == self:
                return True
            category = parent

        return False

class ProductProduct(models.Model):
    _inherit = 'product.template'

    @api.multi
    @api.depends('seller_ids')
    def _calc_primary_supplier(self):
        for prod in self:
            first_supplier = prod.seller_ids and prod.seller_ids[0]

            if not first_supplier:
                continue

            prod.primary_supplier = first_supplier.name

    primary_supplier = fields.Many2one('res.partner', compute='_calc_primary_supplier', readonly=True)
    # Country of origin used to live in account_fiscal_position_expression.
    country_of_origin = fields.Many2one('res.country', string='Country', related='primary_supplier.country_id')

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _calc_primary_product(self):
        icp = self.env['ir.config_parameter']
        categ = icp.get_param('non_primary_product_category')
        if not categ:
            raise exceptions.UserError(_('Need a config parameter called non_primary_product_category'))
        elif categ == 'None':
            self.primary_product_id = None
            return

        assert categ.startswith('product.category,'), 'The format is product.category,xx'
        model, idd = categ.split(',')
        category = self.env['product.category'].browse(int(idd))

        for invoice in self:
            products = [x.product_id for x in invoice.invoice_line_ids if not category.contains(x.product_id)]
            _logger.info('Invoice %s has these primary products %s', invoice, products)
            invoice.primary_product_id = products and products[0]

    @api.multi
    def _calc_country_of_origin(self):
        for invoice in self:
            country_of_origin = None
            pri_product = invoice.primary_product_id
            if pri_product:
                pri_supplier = pri_product.primary_supplier
                if pri_supplier and pri_supplier.country_id:
                    country_of_origin = pri_supplier.country_id
                else:
                    _logger.info('No primary supplier for product %s', pri_product)
            else:
                _logger.info('No primary product for invoice %s', invoice)
            _logger.info('Country of origin for invoice %s is set to %s', invoice, country_of_origin)
            invoice.country_of_origin_id = country_of_origin

    primary_product_id = fields.Many2one(comodel_name='product.product', compute='_calc_primary_product')
    country_of_origin_id = fields.Many2one(comodel_name='res.country', string= 'Country of origin',
                                           compute='_calc_country_of_origin')
