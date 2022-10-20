# -*- coding: utf-8 -*-
{
    "name": "POS Zero Default Cash Opening",
    "version": "0.0.1",
    "category": "Sales/Point of Sale",
    'summary': "Default POS cash opening value to zero, but allow modification",
    "author": "Ewetoye Ibrahim",
    "website": "https://github.com/EwetoyeIbrahim/pos_cash_opening_zero",
    "auto_install": False,
    "depends": ["point_of_sale"],
    'installable': True,
    'application': False,
    'assets': {
        'point_of_sale.assets': [
            'pos_cash_opening_zero/CashOpeningPopup.js',
            ]
    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
}
