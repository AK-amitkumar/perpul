# -*- coding: utf-8 -*-
# Part of Perpul. See LICENSE file for full copyright and licensing details.
{
    'name': 'Perpul-QuickBooks Connector',
    'category': 'Accounting',
    'description': """
QuickBook Connector
====================

Perpul Quickbooks online connector is used to export invoices/bill from Perpul get them paid in QBO and import paid invoices/bills in Perpul.

This module has following features

    1] Import QBO customer into Perpul
    2] Import QBO supplier from QBO into Perpul
    3] Import QBO account into Perpul
    4] Export account into QBO
    5] Import QBO account tax into Perpul
    6] Export account tax into QBO
    7] Export tax agency into QBO
    8] Import QBO product category into Perpul
    9] Import QBO product into Perpul
    10] Import QBO payment method into Perpul
    11] Import QBO payment term into Perpul
    12] Export customer invoice into QBO
    13] Export supplier bill into QBO
    14] Import QBO customer payment into Perpul
    15] Import QBO supplier bill into Perpul

""",
    'author': 'Pragmatic TechSoft Pvt Ltd.',
    'website': 'http://www.pragtech.co.in',
    'currency': 'EUR',
    'license': 'OPL-1',
    'price': 350.00,
    'version': '1.0',
    'depends': ['base', 'sale', 'purchase', 'account'],
    'data': [
        'data/qbo_data.xml',
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/export_partner.xml',
        'views/account_views.xml',
        'views/product_views.xml',
    ],
    'images': ['static/description/flectraquickbook_v11.jpg'],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
