{
    'name': 'ERP',
    'version': '1.0.0',
    'summary': 'test erp',
    'sequence': 100,
    'category': 'Website',
    'description': 'Fixed Color to change background and text color',
    'website': 'https://www.code-flex.com/',
    'depends': [
        'base_setup',
        'sale',
        'purchase',
        'account'
    ],
    'data': [
        'views/menu.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'MRM',
    'maintainer': 'MRM',

}
