# Propagación Analítica MTO en Compras (MBA Consultings)

Módulo complementario para Odoo 19 Community que asegura la trazabilidad de costos en flujos Bajo Pedido (Make To Order / MTO):

- Propaga automáticamente el campo `analytic_distribution` desde la línea de venta (`sale.order.line`) o el proyecto (`sale.order.project_id`) hacia la línea de compra (`purchase.order.line`).
- Se integra de forma nativa con el módulo `purchase_analytic` de la OCA: cuando la orden de compra MTO es generada, la cabecera adopta automáticamente la cuenta analítica del proyecto.
