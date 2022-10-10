# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    request_product_qty = fields.Float(string='Quantity Request', required=True, default='1')

    @api.onchange('request_product_qty', 'product_id')
    def _calcilate_product_qty(self):
        if self.product_id:
            if self.product_id.package:
                self.product_qty = self.product_id.package * self.request_product_qty



