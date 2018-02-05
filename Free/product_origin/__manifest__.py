# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.flectramod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product Origin',
    "summary": "Product Origin",
    "version": "1.0",
    "category": "Sales",
    "website": "http://www.flectramod.com/",
    'description': """
Product Origin
""",
    'author': "Jarvis (www.flectramod.com)",
    'website': 'http://www.flectramod.com',
    'license': 'AGPL-3',
    "depends": [
        'product',
    ],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    "data": [
        'views/product_views.xml'
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
