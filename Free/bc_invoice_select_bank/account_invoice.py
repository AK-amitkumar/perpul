# -.- encoding: utf-8 -.-

from openerp import models, fields, exceptions, api, _
import base64
import StringIO
import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'


    @api.model
    def default_get(self, all_fields):
        _logger.info('default_get %s %s', self._context, all_fields)
        rec = super(AccountInvoice, self).default_get(all_fields)
        _logger.info('REC %s', rec)
        if 'type' in rec and rec['type'] not in ('out_invoice', 'out_refund'):
            return rec

        if 'company_id' not in rec:
            company = self.env.user.company_id
        else:
            assert rec['company_id']
            company = self.env['res.company'].browse(rec['company_id'])

        if 'currency_id' not in rec:
            currency = company.currency_id
        else:
            assert rec['currency_id']
            currency = self.env['res.currency'].browse(rec['currency_id'])

        payable_bank = self.get_payable_bank(company, currency)
        rec['payable_bank_id'] = payable_bank.id
        return rec


    @api.multi
    def invoice_validate(self):
        # If it is a customer invoice it must have payable_bank_id
        for invoice in self:
            if invoice.type == 'out_invoice' and not invoice.payable_bank_id:
                raise exceptions.UserError(
                    _("Customer Invoices must have a payable bank account set."))

        return super(AccountInvoice, self).invoice_validate()

    @api.one
    @api.constrains('payable_bank_id')
    def check_payable_bank(self):
        if not self.payable_bank_id:
            return

        if self.payable_bank_id.currency_id:
            if self.payable_bank_id.currency_id != self.currency_id:
                raise exceptions.ValidationError(_('Wrong bank account. '
                                                   'Bank currency %s Invoice currency %s')
                                                 % (self.payable_bank_id.currency_id.name,
                                                    self.currency_id.name))

    @api.multi
    def get_payable_bank(self, company=None, currency=None):
        if not company:
            self.ensure_one()
            company = self.company_id
            currency = self.currency_id

        for journal in company.bank_journal_ids:
            if not journal.display_on_footer:
                continue

            bank_acc = journal.bank_account_id
            if journal.currency_id == currency:
                _logger.info('Selected bank %s for invoice %s (company %s currency %s)',
                             journal.name, self, company, currency)
                return journal
            else:
                _logger.info('Not using bank %s because of currency', journal)

        for journal in company.bank_journal_ids:
            if not journal.display_on_footer:
                continue

            if journal.currency_id:
                _logger.info('Not using bank %s because it has currency', journal)
                continue

            _logger.info('Selected bank %s [%s] for invoice %s', journal.name, journal.currency_id, self)
            return journal

        # No journal matching
	    raise exceptions.UserError(_('Not able to determine payable bank account'))

    @api.onchange('company_id', 'currency_id')
    def update_payable_bank(self):
        self.ensure_one()
        if self.state != 'draft':
            return

        _logger.info('Trying to determine bank for invoice %s currency %s company %s',
                     self, self.currency_id, self.company_id)
        journal = self.get_payable_bank()
        self.payable_bank_id = journal

    payable_bank_id = fields.Many2one('account.journal', string='Payable to',
                                      required=False, readonly=True,
                                      #default=lambda self: self.get_payable_bank(),
                                      states={'draft': [('readonly', False) ]},
                                      domain="[('company_id', '=', company_id), ('type', '=', 'bank')]")

# domain="[('type', 'in', {'out_invoice': ['bank'], 'out_refund': ['sale'], 'in_refund': ['purchase'], 'in_invoice': ['purchase']}.get(type, [])), ('company_id', '=', company_id)]")
