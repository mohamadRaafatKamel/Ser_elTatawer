# -*- coding: utf-8 -*-
from odoo import api, fields, models,_
from odoo.exceptions import UserError


class MRMProductTemp(models.Model):
    _name = "mrm.product.template"
    _description = "MRM Product"

    name = fields.Char(string='Name', tracking=True, required=True)

    category_ids = fields.One2many("mrm.product.category", 'mrm_product_id')

    # override method
    # @api.model
    def write(self, vals):
        """Override default Odoo write function and extend."""

        # Update Maen name in products
        if "name" in vals:
            for cat in self.category_ids:
                cat.product_template_id.name = vals['name'] + " " + cat.name

        return super(MRMProductTemp, self).write(vals)

    def unlink(self):
        raise UserError(_("You can't delete product"))

