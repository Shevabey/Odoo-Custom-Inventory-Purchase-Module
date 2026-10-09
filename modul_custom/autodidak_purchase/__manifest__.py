{
    'name': 'Module Custom Purchase',
    'version': '14.0.1.0.0',
    'category': 'purchase',
    'summary': 'Purchase Costum Module',
    'description': """
        Purchase Custom Module By Auto Didak
    """,
    'website': '',
    'author': 'Autodidak Channel',
    'depends': ['web', 'base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/autodidak_purchase_view.xml',
        'views/autodidak_purchase_action.xml',
        'views/autodidak_purchase_menuitem.xml',
        'views/autodidak_purchase_sequence.xml',
        'views/autodidak_purchase_cron.xml',
        'reports/autodidak_report_pdf.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}