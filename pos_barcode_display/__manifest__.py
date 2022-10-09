# -*- coding: utf-8 -*-
{
    "name": "Display Barcode on the POS Screen",
    "version": "0.0.1",
    "category": "Sales/Point of Sale",
    'summary': "Include barcode on product items and order line",
    "author": "Ewetoye Ibrahim",
    "website" : "https://github.com/EwetoyeIbrahim/odoo_mathsend/tree/15.0/pos_barcode_display",
    "auto_install": False,
    "depends": ["point_of_sale"],
    'installable': True,
    'application': False,
    'assets': {
        'point_of_sale.assets': [
            'pos_barcode_display/static/src/js/models.js',
            ],
        'web.assets_qweb': [
            'pos_barcode_display/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}
