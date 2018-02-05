# -*- coding: utf-8 -*-
{
    'name': "Plugin for Professional Templates + Invoice Delivery Date",
    'support': "support@optima.co.ke",

    'summary': """
        Once you purchase 'Professional Report Templates' and 'Add Delivery Date on Invoice', you will need this Free plugin to print delivery date on invoices """,

    'description': """
        Once you purchase `Professional Report Templates` and `Add Delivery Date on Invoice`, you will need this Free plugin to print delivery date on invoices
    """,

    'author': "Optima ICT Services LTD",
    'website': "http://www.optima.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
