# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',

    'summary': """Academy app to manage training""",

    'description': """
        Academy Module to manage training
        -Courses
        -Session
        -Attendes
    """,

    'author': 'SL',
    'website': 'http://www.odoo.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/academy_demo.xml',
    ],
}