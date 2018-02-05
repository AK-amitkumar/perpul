# -*- coding: utf-8 -*-

from flectra import fields, models


class ProjectTask(models.Model):

    _inherit = 'project.task'

    product_ids = fields.Many2many('product.product', string="Products")
