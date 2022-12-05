# -*- coding: utf-8 -*-
{
    "name": "Nigeria Localization",
    "version": "0.0.1",
    "category": "Localizations",
    'summary': "Set Nigerian states and lagos state LG and LCDA as cities",
    "author": "Ewetoye Ibrahim",
    "website" : "https://github.com/EwetoyeIbrahim/odoo_mathsend",
    "auto_install": False,
    "depends": ["base_address_city"],
    'installable': True,
    'application': False,
    'data': [
        'data/res.country.state.csv',
        'data/res.city.csv',
        'data/res_country_data.xml',
        'views/res_partner_views.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.jpg'],
}
