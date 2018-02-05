import logging
from openerp import models, api, _, fields
import arrow

_logger = logging.getLogger(__name__)


class bc_confirm_and_send(models.Model):
    _name = 'bc_confirm_and_send_so.bc_confirm_and_send'

    @api.model
    def scheduler_tick_orders(self):
        icp = self.env['ir.config_parameter']
        ai = self.env['account.invoice']
        so = self.env['sale.order']

        extra_emails = icp.get_param('bc_confirm_and_send_so_etra_emails')
        demand_vat = icp.get_param('bc_confirm_and_send_so_require_vat')
        _logger.info('Is VAT number required by bc_confirm_and_send? %s ( bc_confirm_and_send_so_require_vat )', demand_vat)

        if not extra_emails:
            _logger.info(
                'You can configure extra emails for SO confirmation by adding parameter bc_confirm_and_send_so_etra_emails')
        _logger.info('Language %s', self.env.context)

        mail_template = self.env['mail.template'].search([('model', '=', 'account.invoice')])
        _logger.info('mail_template %s', mail_template)
        emails = extra_emails and extra_emails.split(',') or []

        # First, confirm
        for order in so.search([('state', '=', 'sent')]):
            # If this is a customer registered from Perpul eCommerce it will have company_name
            # The create_company will make a real company.
	    vat1 = order.partner_invoice_id.vat
	    order.partner_invoice_id.create_company()
            if order.partner_invoice_id.parent_id:
		_logger.info('Checking for parent email')
                if not order.partner_invoice_id.parent_id.email:
                   partner_email = order.partner_invoice_id.email
                   if partner_email:
                      _logger.info('Partner has email %s but parent has none. Copying', partner_email)
                      order.partner_invoice_id.parent_id.email = partner_email

                _logger.info('Setting invoice partner')
                order.partner_invoice_id = order.partner_invoice_id.parent_id
                vat2 = order.partner_invoice_id.vat
                if not vat2 and vat1:
                   order.partner_invoice_id.vat = vat1

            if demand_vat:
                if not order.partner_invoice_id.vat:
                   raise exceptions.UserError(_('We must have VAT number for partner %s') % order.partner_invoice_id)

            _logger.info('Confirming order %s', order.name)
            order.action_confirm()

        #ctx_company = {'company_id': tx.sale_order_id.company_id.id,
        #            'force_company': tx.sale_order_id.company_id.id}

        for order in so.search([('invoice_status', '=', 'to invoice')]):
            if order.invoice_ids:
               _logger.info('Sale Order %s already has invoices %s, so it is strange it has invoice_status == to invoice', order.name, order.invoice_ids)
               continue
            _logger.info('Creating invoice for order %s', order)
            created_invoice = order.action_invoice_create()
            created_invoice = self.env['account.invoice'].browse(created_invoice)
            if created_invoice:
                created_invoice.action_invoice_open()

        for invoice in ai.search([('state', '=', 'open'), ('sent', '!=', True)]):
            template = mail_template.sudo().with_context(
                #lang = follower.lang,
                #template_type = "follower",
                #email_from_usr = email_from_usr,
                #email_from_mail = email_from_mail,
                #email_from = email_from,
                #email_to = 'torvald@bringsvor.com',
                #link = "sign/document/%(request_id)s/%(access_token)s" % {'request_id': self.id, 'access_token': self.access_token},
                #subject = subject or ("Signature request - " + self.reference),
                #msgbody = (message or "").replace("\n", "<br/>")
            )
            _logger.info('using template %s', template.name)
            source = invoice.origin
            msg_text = None
            if source:
                so = self.env['sale.order'].search([('name', '=', source)])
                if so:
                    msg = [x.body for x in so.message_ids if x.body.find('soknad')!=-1 ]
                    if msg:
                        #msg2 = BeautifulSoup(msg)
                        msg_text = msg[0]

            rendered = template.with_context(email_to='torvald@bringsvor.com').generate_email(invoice.id, {'email_to': 'torvald@bringsvor.com'})

            rendered['body_html'] = _('Vennligst se vedlagte faktura fra %s. Utsendelsestidspunkt %s') % \
                                    (invoice.company_id.name,
                                     arrow.now().format('YYYY-MM-DD HH:mm'))
            rendered['subject'] = _('Faktura %s') % invoice.number
            # A small hack
            if not 'email_from' in rendered:
                rendered['email_from'] = template['email_from']

            _logger.info('ATTACH %s', rendered['attachments'])
            attid = []
            for att in rendered['attachments']:
                # filename - data
                filename, pdfdata = att
                att2 = self.env['ir.attachment'].create({
                    'name': filename,
                    'datas_fname': filename,
                    'res_model': 'account.invoice',
                    'datas': pdfdata,
                    'res_id': invoice.id,
                })
                attid.append(att2.id)
            attachment_ids = [(6, 0, attid)]

            rendered['attachment_ids'] = attachment_ids

            #rendered['email_from'] = 'mersmak@provendo.no' # Why is this needed?
            _logger.info('Sending invoice from email %s', rendered['email_from'])
            rendered['reply_to'] = rendered['email_from']
            partner_email = invoice.partner_id.email or ''
            _logger.info('Sending invoice %s to %s', invoice.number, partner_email)
            rendered['email_to'] = partner_email
            themsg = self.env['mail.mail'].create(rendered)
            themsg.send()
            phone = invoice.partner_id.mobile or invoice.partner_id.phone or ''
            thebody = rendered['body_html']
            if msg_text:
                thebody = msg_text + thebody

            rendered['body_html'] = _('<p>Email sent to customer %s (%s) (%s) </p>%s') % \
                (invoice.partner_id.name, invoice.partner_id.email, phone, thebody)

            for email in emails:
                _logger.info('Sending invoice %s to %s', invoice.number, email)
                rendered['email_to'] = email

                themsg = self.env['mail.mail'].create(rendered)
                themsg.send()
            invoice.sent = True
            i2 = ai.browse(invoice.id)
            assert i2.sent
            _logger.info('Flagged invoice %s as sent', invoice.number or invoice)
