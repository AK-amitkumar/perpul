# -*- coding: utf-8 -*-
# module template
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Invoices Paid Amounts',
    'version': '11.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'author': "Perpul Tips",
    'website': 'http://www.gotflectra.com/',
    'depends': ['base', 'mail', 'account',
                ],
    'images': ['images/main_screenshot.png'],
    'data': [
             'views/account_invoice_view.xml',
             ],
    'installable': True,
    'application': True,
}
