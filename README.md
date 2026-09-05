# Propagación Analítica MTO en Compras (MBA Consultings)

Módulo complementario para **Odoo 19.0 Community** diseñado por **MBA Consultings** para garantizar la trazabilidad de costos en flujos **Bajo Pedido (Make To Order / MTO)**.

---

## 🚀 Funcionalidad Principal

En Odoo estándar, cuando se confirma un Pedido de Venta (`sale.order`) con productos configurados en ruta Bajo Pedido (MTO), las Órdenes de Compra generadas automáticamente no heredan la distribución analítica ni el proyecto asignado a la venta.

Este micro-módulo resuelve esa brecha:

1. **Propagación Automática:** Intercepta la regla de abastecimiento MTO en `purchase.order.line._prepare_purchase_order_line_from_procurement`.
2. **Hereda la Distribución Analítica:** Lee el campo `analytic_distribution` (JSON) de la línea del pedido de venta (`sale.order.line`) o del proyecto asociado (`sale.order.project_id`).
3. **Inyección en Líneas de Compra:** Asigna el 100% de la analítica del proyecto a cada línea de compra generada al proveedor.
4. **Sincronización con Cabecera:** Se integra de forma nativa con `purchase_analytic` (de la OCA) para que el campo *Distribución Analítica* de la cabecera de la orden de compra refleje automáticamente el proyecto.

---

## 📦 Dependencias

* `purchase_stock` (Odoo Core)
* `sale_purchase_stock` (Odoo Core)
* `purchase_analytic` (OCA / `account-analytic`)

---

## 🛠️ Instalación y Uso

1. Colocar el módulo en la ruta de addons de Odoo 19 (ej. `/mnt/extra-addons`).
2. Actualizar lista de aplicaciones en Odoo.
3. Instalar **`mba_purchase_mto_analytic`** (se instalarán automáticamente sus dependencias).

### Flujo de Operación:
1. Crear un Pedido de Venta o cotización de Proyecto Solar.
2. Asignar el Proyecto o Cuenta Analítica en la venta.
3. Confirmar la Venta.
4. La Orden de Compra generada al proveedor tendrá asignado el Proyecto en la cabecera y en cada línea.

---

## 📄 Licencia y Autor
* **Autor:** MBA Consultings (Brooks Gonzalez)
* **Licencia:** AGPL-3
* **Repositorio:** [https://github.com/DevOpsMBAConsultings/mba_purchase_mto_analytic](https://github.com/DevOpsMBAConsultings/mba_purchase_mto_analytic)
