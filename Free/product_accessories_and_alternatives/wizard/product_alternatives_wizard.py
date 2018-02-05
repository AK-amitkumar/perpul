# -*- coding: utf-8 -*-

from flectra import api, fields, models


class product_alternatives_wizard(models.TransientModel):
    _name = 'product.alternatives.wizard'
    _description = 'Product Alternatives'

    def _default_alternative_product_ids(self):
        return self.env['product.template'].browse(self._context.get('active_id')).alternative_product_ids

    alternative_product_ids = fields.Many2many(
        'product.template',
        'product_alternatives_wizard_rel',
        'src_id',
        'dest_id',
        string='Alternative Products',
        default=lambda self: self._default_alternative_product_ids(),
    )

    @api.multi
    def apply_changes(self):
        if self._context.get('active_model'):
            product_id = self.env['product.template'].browse(self._context.get('active_id'))
            product_id.alternative_product_ids = [(6, 0, self.alternative_product_ids.ids)]
