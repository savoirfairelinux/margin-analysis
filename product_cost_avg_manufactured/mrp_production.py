# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import orm


class Production(orm.Model):
    _inherit = 'mrp.production'
    _name = 'mrp.production'

    def action_produce(self, cr, uid,
                       production_id, production_qty, production_mode,
                       context=None):
        res = super(Production, self).action_produce(
            cr, uid,
            production_id, production_qty, production_mode,
            context=context)

        if production_mode == "consume_produce":
            production = self.browse(cr, uid, production_id, context=context)
            product = production.product_id

            production_cost = sum(
                line.product_id.standard_price * line.product_qty
                for line in production.bom_id.bom_lines
            )
            old_cost = product.standard_price

            new_inventory = product.qty_available
            orig_qty = new_inventory - production_qty

            new_cost = (
                old_cost * orig_qty + production_cost * production_qty
            ) / new_inventory

            product.write({'standard_price': new_cost})

        return res
