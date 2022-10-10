{
    'name': 'Ser ERP',
    'version': '1.0.0',
    'summary': 'Ser ERP',
    'sequence': 100,
    'category': 'Website',
    'description': 'Ser ERP',
    'website': 'https://www.code-flex.com/',
    'depends': [
        'base_setup',
        'product',
        'uom',
        'purchase',
        'stock',
        'mrm_ser_eltatawer_erp'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/product.xml',
        'views/tmp_product.xml',

        'views/purchase.xml',
        'views/sales.xml',


        'views/menu.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'Code Flex',
    'maintainer': 'MRM',

}
