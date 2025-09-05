{
    'name': 'Tanzania - Accounting Reports',
    'countries': ['tz'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting report for Tanzania
    """,
    'depends': [
        'l10n_tz_account',
        'account_reports',
    ],
    'data': [
        "data/balance_sheet.xml",
        "data/profit_loss.xml",
    ],
    'installable': True,
    'auto_install': True,
    'website': 'https://www.odoo.com/app/accounting',
    'license': 'OEEL-1',
}
