# -*- coding: utf-8 -*-
from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def _prepare_purchase_order_line_from_procurement(
        self, product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values, po
    ):
        res = super()._prepare_purchase_order_line_from_procurement(
            product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values, po
        )
        sale_line_id = values.get("sale_line_id")
        if sale_line_id:
            sale_line = self.env["sale.order.line"].browse(sale_line_id)
            if sale_line.analytic_distribution:
                res["analytic_distribution"] = sale_line.analytic_distribution
            elif sale_line.order_id.project_id and sale_line.order_id.project_id.analytic_account_id:
                res["analytic_distribution"] = {
                    str(sale_line.order_id.project_id.analytic_account_id.id): 100.0
                }
        return res
