# Copyright 2019 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
from odoo.addons.datamodel.fields import NestedModel


class VehicleInfo(Datamodel):
    _name = "vehicle.info"
    _inherit = "vehicle.short.info"

    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    active = fields.Boolean(required=True)
    company_id = fields.Integer(required=True)
    currency_id = fields.Integer(required=True)
    license_plate = fields.String(required=True)
    vin_sn = fields.String(required=True)
    driver_id = fields.Integer(required=True)
    future_driver_id = fields.Integer(required=True)
    model_id = fields.Integer(required=True)
    manager_id = fields.Integer(required=True)
    brand_id = fields.Integer(required=True)
