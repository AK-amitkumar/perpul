# -*- coding: utf-8 -*-
{
    'name': "Wordpress Migration - Blog Posts",
    'version': "1.0.2",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary': "Copies Wordpress blog posts and comments into Perpul",
    'description': "Copies Wordpress blog posts and comments into Perpul",
    'license':'LGPL-3',
    'data': [
        'views/migration_import_wordpress_views.xml',
    ],
    'demo': [],
    'depends': ['migration_wordpress', 'website_blog'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}    