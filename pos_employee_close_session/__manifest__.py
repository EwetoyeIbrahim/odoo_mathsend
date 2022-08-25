# -*- coding: utf-8 -*-
{
    "name": "Employee Close Point of Sale Session",
    "version": "0.0.1",
    "category": "Sales/Point of Sale",
    'summary': "Allow employees access to close session button",
    'description': "",
    "author": "Ewetoye Ibrahim",
    "website": "https://github.com/EwetoyeIbrahim/pos_employees_close_session",
    "auto_install": False,
    "depends": ["point_of_sale", "pos_hr"],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_employee_close_session/Chrome.js',
            ],
    },
    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
}
