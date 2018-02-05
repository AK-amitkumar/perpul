{
    'name': 'Automatic Workflow Settings',
    'version': '11.0',
    'category': 'Sale',
    'license': 'OPL-1',
    'description': """    
    """,
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',
    'depends': ['sale','account','stock'], 
    'init_xml': [],
    'data': [ 
            'view/sale_workflow_process_view.xml',
            'view/automatic_workflow_data.xml',
            'view/sale_view.xml',
		    'view/transaction_log_view.xml',
            'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'images': ['static/description/main_screen.jpg']
}

