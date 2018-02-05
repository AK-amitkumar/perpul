# -*- coding: utf-8 -*-

{
    'name': 'Invoice Select Bank',
    'author': 'Bringsvor Consulting AS',
    'website': 'www.bringsvor.com',
    'category': 'account',
    'summary': 'Show the bank field on the invoice and make it selectable.',
    'version': '1.0',
    'description': """Select bank account""",
    'depends': ['account'],
    'data': [
	'views/account_invoice.xml',
    ],
    'installable': True,
    #'price': 100.00,
    #'currency': 'EUR',
}
