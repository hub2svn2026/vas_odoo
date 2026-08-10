# -*- coding: utf-8 -*-
{
    'name': 'VAS - Vietnamese Accounting Standards',
    'icon': '/vas_accounting_public/static/description/icon.png',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'VAS - Kế toán Việt Nam | Giải pháp kế toán tích hợp theo chuẩn mực kế toán Việt Nam (VAS).',
    'author': 'Hub2S Vietnam Co., Ltd',
    'website': 'https://hub2s.com/giai-phap-vas',
    'license': 'OPL-1',
    'depends': [
        'stock',
        'account',
        'account_accountant',
        'purchase',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/vas_security.xml',
        'views/vas_payment_required.xml',
        'views/vas_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'vas_accounting_public/static/src/js/vas_payment_required.js',
        ],
    },
    'images': [
        'vas_accounting_public/static/description/cover.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
