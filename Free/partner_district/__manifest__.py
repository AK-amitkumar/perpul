# -*- coding: utf-8 -*-
# module template
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner District',
    'version': '11.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'author': "Perpul Tips",
    'website': 'http://www.gotflectra.com/',
    'depends': ['base', 'sale', 'sale_management'
                ],

    'images': ['images/main_screenshot.png'],
    'data': [
             'views/res_partner_view.xml',
             ],
    'installable': True,
    'application': True,
}
