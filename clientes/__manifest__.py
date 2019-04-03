# -*- coding: utf-8 -*-
{
    'name': "clientes",
   'summary': """
        Modulo para manejo de clientes.
    """,
    'description': """
        modulo se encargara de registrar todo los clientes con lo que cuenta la empresa llevando un control mas ordenado de sus clientes
    """,
    'author': "William y Sergio",
    'category': 'Clientes',
    'version': '10.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'muk_web_theme'],

    # always loaded
    'data': [
        #'data/hn_sale_data.xml',
        #'data/hn_sale_sequence.xml',
        'security/rules.xml',
        'security/ir.model.access.csv',
        
        #'wizard/consolidate_orders.xml'
        #'report/report_layout.xml',
        #'report/account_invoice.xml',
        #'report/poa_report_templates.xml',
        #'report/poa_report_pivot.xml',
        #'report/pei_pivot.xml',
        'views/cliente.xml',
        
    ],
    # only loaded in demonstration mode
    
}