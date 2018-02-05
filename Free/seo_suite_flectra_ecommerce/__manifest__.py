{   
    'name': "SEO Suite Perpul eCommerce",
    'category': 'Website',
    'version': '1.0',
    'license': 'OPL-1',
    'summary' : 'Perpul SEO suite helps you automate all the basic on-page SEO aspects of you flectra eCommerce store. From solving duplicate content issues to advanced SEO templates.',
    'description': """
    """,
    'depends': ['website_sale','product'],

    'data': [
             'data/seo_globle_variable_data.xml',
             'views/seo_product_template.xml',
             'views/templates.xml',
             'views/seo_template_setting.xml',
             'security/ir.model.access.csv',
           ],

    'author' : "Emipro Technologies Pvt. Ltd.",
    'website': 'http://www.emiprotechnologies.com/',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',
    'images': ['static/description/Seo_flectra_store_covor.jpg'],    
    'installable': True,
    'auto_install': False,
    'application' : True,
   
}
