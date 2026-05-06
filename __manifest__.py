# -*- coding: utf-8 -*-
{
    'name': 'Password Eyes Icon Widget',
    'version': '1.1',
    'summary': 'Adds an eye icon to toggle visibility for password fields in Odoo 16.',
    'description': """
Adds a custom field widget for backend forms and a visibility toggle icon
to the password field on the public Login page.

Features:
- Backend widget for password fields via 'password_eyes_icon' widget attribute
- Login page password visibility toggle (injects icon on existing input)
    """,
    'category': 'Extra Tools',
    'author': 'Gout',
    'license': 'LGPL-3',
    'depends': [
        'web',
    ],
    'data': [
        'views/web_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'password_eyes_icon/static/src/scss/password_eyes_icon.scss',
            'password_eyes_icon/static/src/js/password_eyes_icon_field.js',
            'password_eyes_icon/static/src/xml/password_eyes_icon.xml',
        ],
        'web.assets_frontend': [
            'password_eyes_icon/static/src/scss/password_eyes_icon.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [
        'static/description/thumbnail.png',
    ],
}
