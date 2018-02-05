# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################

from flectra import fields , models,api
from flectra.exceptions import ValidationError


class ChannelPricelistMappings(models.Model):
	_name="channel.pricelist.mappings"
	_order = 'need_sync'
	_rec_name='flectra_pricelist_id'
	@api.model
	def _needaction_domain_get(self):
		return [('need_sync', '=', 'yes')]

	@api.model
	def ecom_storeUsed(self):
		channel_list = []
		channel_list = self.env['multi.channel.sale'].get_channel()
		return channel_list

	name = fields.Char(
		compute='_compute_name'
	)
	store_currency  =  fields.Many2one(
		'res.currency',
		string='Store Currency',
		required=True
	)
	store_currency_code =  fields.Char(
		'Store Currency Code',
		related='store_currency.name',
		required=True
	)
	flectra_pricelist_id = fields.Many2one(
		'product.pricelist',
		string='Perpul Pricelist',
		required=True
	)
	flectra_currency = fields.Many2one(
		'res.currency',
		related='flectra_pricelist_id.currency_id',
		string='Perpul Currency',
		required=True
	)
	flectra_currency_id = fields.Integer(
		string='Perpul Currency ID',
		required=True
	)
	channel_id = fields.Many2one(
		'multi.channel.sale',
		string='Instance',
		required=True
	)
	ecom_store = fields.Selection(
		'ecom_storeUsed',
		string="Channel",
		related='channel_id.channel',
		required=True, store=True
	)
	need_sync = fields.Selection(
		(('yes','Yes'),('no','No')),
		string='Update Required',
		default='no'	,
		required=True
	)
	@api.onchange('flectra_currency')
	def set_flectra_currency_id(self):
		self.flectra_currency_id = self.flectra_currency.id

	def _compute_name(self):
		for record in self:
			if record.flectra_currency:
				record.name = record.flectra_currency.name
			else:
				record.name = 'Deleted'
