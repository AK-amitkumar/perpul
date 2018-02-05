# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2017-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
# Developed By: Jahangir Ahmad
#################################################################################
from flectra import fields , models,api
from flectra.exceptions import ValidationError
PartnerType = [
	('contact','Contact'),
	('invoice','Invoice'),
	('delivery','Delivery'),
]
class ChannelOrderMappings(models.Model):
	_name="channel.partner.mappings"
	_inherit = ['channel.mappings']
	type = fields.Selection(
		selection = PartnerType,
		default='contact',
		required=1
	)
	store_customer_id =  fields.Char('Store Customer ID',required=True)
	flectra_partner_id = fields.Integer(string='Perpul Partner ID',required=True)
	flectra_partner = fields.Many2one('res.partner',string='Perpul Partner', required=True)
	_sql_constraints = [
		('channel_store_customer_id_uniq',
		'unique(channel_id, store_customer_id,type)',
		'Store partner ID must be unique for channel partner mapping!'),
		# ('channel_flectra_partner_id_uniq',
		#   	'unique(channel_id, flectra_partner_id)',
		#   	'Perpul partner ID must be unique for channel partner mapping!'),
	]

	@api.onchange('flectra_partner')
	def change_flectra_id(self):
		self.flectra_partner_id = self.flectra_partner.id

	def _compute_name(self):
		for record in self:
			if record.flectra_partner:
				record.name = record.flectra_partner.name
			else:
				record.name = 'Deleted'
