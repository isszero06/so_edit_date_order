# -*- coding: utf-8 -*-
{
    'name': 'Sales Order Date Order Visible and Editable',
    'version': '13.0.1.0',
    'category': 'sale',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """If Sales order Date less than today date and when confirm order the order date not change""",

    'description': """
        In the Odoo system, you cannot record sales orders retroactively “with old dates” ,

        you can only see the date field when the sales order is confirmed and you cannot modify it,

        but with our development you can edit the date of the order when creating the order, 

        which is in the case of a price quote and when the sales order is confirmed if it is The date of the sale order is less than today's

        date, the sale order will be confirmed on this date, otherwise the sale order will be confirmed on today's date

        """,
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/sale_order.xml',
    ],
    'license': 'OPL-1',
    'live_test_url': 'https://www.youtube.com/watch?v=T82sTeIwrm8',
    'images': ['static/description/logo.PNG'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 25.0,
    'currency': 'USD',
}
