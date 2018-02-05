# -*- coding: utf-8 -*-

{
    'name': 'Product Primary',
    'author': 'Bringsvor Consulting AS',
    'website': 'www.bringsvor.com',
    'category': 'Sale',
    'summary': 'Determine which is a primary product of an invoice.',
    'version': '1.2',
    'description': """Primary product""",
    'depends': ['account', 'sale', 'product'],
    'data': [
        'views/account_invoice.xml',
	'views/product.xml',
    ],
    'installable': True,
#    'price': 100.00,
#    'currency': 'EUR',
}
