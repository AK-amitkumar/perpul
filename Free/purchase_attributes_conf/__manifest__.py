# -*- coding: utf-8 -*-
{
    'name': 'Purchase Attributes',
    'version': '1.1',
    'category': 'Purchases',
    'summary': 'Purchase managers might manage product attributes',
    'description': '''
    The app is a tool to let your purchase managers create,
    edit and delete product attributes and attribute values through the special configuration menus in Purchases.
    ''',
    'auto_install': False,
    'author': 'IT Libertas',
    'website': 'https://flectratools.com',
    'depends': [
        'purchase',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/purchase_menuitems.xml',
    ],
    'qweb': [

    ],
    'js': [

    ],
    'demo': [

    ],
    'test': [

    ],
    'license': 'Other proprietary',
    'images': [
        'static/description/main.png',
    ],
    'update_xml': [

    ],
    'application': False,
    'installable': True,
    'private_category': False,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'post_load': 'post_load',
    'uninstall_hook': 'uninstall_hook',
    'external_dependencies': {
    },

}
