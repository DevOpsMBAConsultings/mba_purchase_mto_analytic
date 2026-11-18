# -*- coding: utf-8 -*-
{
    'name': "Propagación Analítica MTO en Compras (MBA Consultings)",
    'summary': "Pasa automáticamente la distribución analítica de la línea o proyecto de venta a la orden de compra y transferencias de almacén",
    'version': "19.0.1.0.0",
    'category': "Purchases",
    'author': "MBA Consultings",
    'website': "https://mbaconsultings.com",
    'license': "AGPL-3",
    'depends': [
        'purchase_stock',
        'sale_purchase_stock',
        'purchase_analytic',
        'stock_picking_analytic',
        'sale_project',
    ],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
