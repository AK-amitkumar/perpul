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
class ChannelShippingMappings(models.Model):
	_name="channel.shipping.mappings"
	_inherit = ['channel.mappings']
	_rec_name = 'shipping_service'
	flectra_carrier_id = fields.Integer(string='Perpul Carrier ID')
	flectra_shipping_carrier = fields.Many2one('delivery.carrier',string='Perpul Shipping Carrier', required=True)
	shipping_service = fields.Char("Store Shipping Service")
	shipping_service_id = fields.Char("Shipping Serivce ID")
	international_shipping = fields.Boolean('Is International')

	def _compute_name(self):
		for record in self:
			if record.flectra_shipping_carrier:
				record.name = record.flectra_shipping_carrier.name
			else:
				record.name = 'Deleted'

	@api.onchange('flectra_shipping_carrier')
	def change_flectra_id(self):
		self.flectra_carrier_id = self.flectra_shipping_carrier.id
