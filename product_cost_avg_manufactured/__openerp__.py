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

{
    "name" : "Product Cost Average Manufacturing Price",
    "version" : "1.0",
    "author" : "Savoir-faire Linux",
    "category" : "Generic Modules/Inventory Control",
    "depends" : [
        "mrp",
    ],
    "description": """
Product Cost Average Manufacturing Price
========================================

This module allows computing the standard price of products based on their
average (weighted) manufacturing cost. The formula used to calculate the
new cost when a production is made is the following:

    New Cost = (Old Cost * Inventory + Production Unit Cost * Production Qty)
                -------------------------------------------------------------
                                    New Inventory

Contributors
------------

* Vincent Vinet <vincent.vinet@savoirfairelinux.com>

""",
    'demo': [
    ],
    'data': [
    ],
    'test': [
        'test/price_historization.yml',
        'test/cost_price_update.yml',
        'test/price_controlling_multicompany.yml',
    ],
    'installable': True,
    'auto_install': True,
    'active': False,
}
