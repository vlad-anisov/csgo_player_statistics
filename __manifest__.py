{
    'name': "CSGO Player Statistics",

    'summary': """
        CSGO Player Statistics""",

    'description': """
        CSGO Player Statistics
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'website'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'report/player_reports.xml',
        'report/player_templates.xml',
    ],

    'application': True,

    'post_init_hook': 'load_players',
    
    'external_dependencies': {
        'python': ['beautifulsoup4', 'bs4', 'python-utils', 'six']
    }
}
