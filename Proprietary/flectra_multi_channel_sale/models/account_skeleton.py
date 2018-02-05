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
TaxType = [
	('fixed','Fixed'),
	('percent','Percentage')
]
class ChannelAccountMappings(models.Model):
	_name="channel.account.mappings"
	_inherit = ['channel.mappings']
	store_tax_value_id =  fields.Char('Store Tax Value/ID',required=True)
	flectra_tax_id = fields.Integer(string='Perpul Tax ID',required=True)
	tax_name = fields.Many2one('account.tax', string='Perpul Tax Name', required=True)
	include_in_price = fields.Boolean(string="Include in price")
	tax_type = fields.Selection(
		selection=TaxType,
		string="Tax Type",
		default='percent',
		required=True,
	)
	def _compute_name(self):
		for record in self:
			if record.tax_name:
				record.name = record.tax_name.name
			else:
				record.name = 'Deleted'

	@api.onchange('tax_name')
	def change_flectra_id(self):
		self.tax_name = self.tax_name.id

class ChannelAccountJournalMappings(models.Model):
	_name="channel.account.journal.mappings"
	_inherit = ['channel.mappings']
	store_journal_name =  fields.Char('Store Payment Method',required=True)
	journal_code =  fields.Char('Journal Code',required=True, related="flectra_journal.code")
	flectra_journal_id = fields.Integer('Perpul Journal ID',required=True)
	flectra_journal = fields.Many2one('account.journal',string='Perpul Journal Name', required=True)
	@api.multi
	def _compute_name(self):
		for record in self:
			if record.store_journal_name:
				record.name = record.store_journal_name
			else:
				record.name = 'Deleted'


	@api.onchange('flectra_journal')
	def change_flectra_id(self):
		self.flectra_journal_id = self.flectra_journal.id
