# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_
from odoo.exceptions import UserError


class MRMProductCategory(models.Model):
    _name = "mrm.product.category"
    _description = "MRM Product Category"

    name = fields.Char(string='Name', tracking=True, required=True)
    package = fields.Float(string='Amount', tracking=True, required=True, default="1")
    unit_id = fields.Many2one("uom.uom", string="Unit", required=True)
    haveExpired = fields.Boolean(string='Have Expired', tracking=True)

    havePart = fields.Boolean(string='Have Part', tracking=True)
    amountForPart = fields.Float(string='Amount', tracking=True, default="1")
    partPackage = fields.Integer(string='Amount package', tracking=True)
    partUnit_id = fields.Many2one("uom.uom", string="package Unit ", tracking=True)

    barcode = fields.Char(string='Barcode', tracking=True)

    status = fields.Boolean(string='status', tracking=True, default=True)

    mrm_product_id = fields.Many2one("mrm.product.template", string="Product")
    product_template_id = fields.Many2one("product.template", tracking=True)

    # make package unit and part unit in same unit category
    @api.onchange('unit_id', 'partUnit_id', 'havePart')
    def _onchange_unit_validation(self):
        if self.havePart:
            if self.partUnit_id:
                if self.unit_id.category_id.id != self.partUnit_id.category_id.id:
                    self.partUnit_id = self.unit_id
        else:
            self.partUnit_id = None

    # calculate part amount base on units and package amount
    @api.onchange('unit_id', 'partUnit_id', 'havePart', 'package', 'amountForPart')
    def _onchange_part_amount_validation(self):
        if self.havePart:
            # add amount and part unit and same category
            if self.partUnit_id and self.package and self.amountForPart:
                if self.unit_id.category_id.id == self.partUnit_id.category_id.id:
                    if self.partUnit_id != self.unit_id and self.amountForPart != 0:
                        self.partPackage = ((self.partUnit_id.factor / self.unit_id.factor) * self.package) / self.amountForPart
                    else:
                        self.partPackage = 1
                else:
                    self.partPackage = 1
            else:
                self.partPackage = 0
        else:
            self.partPackage = 0

    # override method
    @api.model
    def create(self, vals):
        """Override default Odoo write function and extend."""

        print(vals)
        mrm_product = self.env['mrm.product.template'].browse(vals['mrm_product_id'])
        record = self.env['product.template'].create({
            'name': mrm_product.name + " " + vals['name'],
            'barcode': vals['barcode'] if 'barcode' in vals else "",
            'haveExpired': vals['haveExpired'] if 'haveExpired' in vals else False,
            'package': vals['package'] if 'package' in vals else None,
            'havePart': vals['havePart'] if 'havePart' in vals else False,
            'amountForPart': vals['amountForPart'] if 'amountForPart' in vals else None,
            'partPackage': vals['partPackage'] if 'partPackage' in vals else None,
            'uom_id': vals['unit_id'],
            'mrm_product_id': vals['mrm_product_id'],
            'uom_po_id': vals['partUnit_id'] if 'partUnit_id' in vals else vals['unit_id'],
            'type': "product",
        })
        vals['product_template_id'] = record.id


        return super(MRMProductCategory, self).create(vals)

    # override method
    # @api.model
    def write(self, vals):
        """Override default Odoo write function and extend."""

        print("cat  - write ", vals)

        if "name" in vals:
            self.product_template_id.name = self.mrm_product_id.name + " " + vals['name']
        if "barcode" in vals:
            self.product_template_id.barcode = vals['barcode']
        if "haveExpired" in vals:
            self.product_template_id.haveExpired = vals['haveExpired']
        if "package" in vals:
            self.product_template_id.package = vals['package']
        if "havePart" in vals:
            self.product_template_id.havePart = vals['havePart']
        if "amountForPart" in vals:
            self.product_template_id.amountForPart = vals['amountForPart']
        if "partPackage" in vals:
            self.product_template_id.partPackage = vals['partPackage']
        if "unit_id" in vals:
            # self.product_template_id.uom_po_id = None
            self.product_template_id.uom_id = vals['unit_id']
        if "partUnit_id" in vals:
            self.product_template_id.uom_po_id = vals['partUnit_id']

        return super(MRMProductCategory, self).write(vals)

    def unlink(self):
        raise UserError(_("You can't delete product"))


