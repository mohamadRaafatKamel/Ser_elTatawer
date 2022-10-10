# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CostCenterProduct(models.Model):
    _inherit = "product.template"

    package = fields.Float(string='Amount', tracking=True, readonly=True)
    unit_id = fields.Many2one("uom.uom", string="Unit", readonly=True)
    haveExpired = fields.Boolean(string='Have Expired', tracking=True, readonly=True)

    havePart = fields.Boolean(string='Have Part', tracking=True, readonly=True)
    amountForPart = fields.Float(string='Amount', tracking=True, readonly=True)
    partPackage = fields.Integer(string='Amount package', tracking=True, readonly=True)
    partUnit_id = fields.Many2one("uom.uom", string="package Unit ", tracking=True, readonly=True)

    mrm_product_id = fields.Many2one("mrm.product.template", string="الماده", tracking=True, readonly=True)



