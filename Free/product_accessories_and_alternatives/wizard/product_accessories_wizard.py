# -*- coding: utf-8 -*-

from flectra import api, fields, models


class product_accessories_wizard(models.TransientModel):
    _name = 'product.accessories.wizard'
    _description = 'Product Accessories'

    def _default_accessory_product_ids(self):
        return self.env['product.template'].browse(self._context.get('active_id')).accessory_product_ids

    accessory_product_ids = fields.Many2many(
        'product.product',
        'product_accessories_wizard_rel',
        'src_id',
        'dest_id',
        string='Accessory Products',
        default=lambda self: self._default_accessory_product_ids(),
    )

    @api.multi
    def apply_changes(self):
        if self._context.get('active_model'):
            product_id = self.env['product.template'].browse(self._context.get('active_id'))
            product_id.accessory_product_ids = [(6, 0, self.accessory_product_ids.ids)]
