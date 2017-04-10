# -*- coding: utf-8 -*-
################################################################
#    License, author and contributors information in:          #
#    __openerp__.py file at the root folder of this module.    #
################################################################

from openerp import models, fields, api, _
from openerp.exceptions import Warning
import openerp.addons.decimal_precision as dp
import logging

_logger = logging.getLogger(__name__)

###############################################################################
#   model.inherit                                                             #
###############################################################################

class ModelInherit(models.Model):

    _inherit = 'res.partner'

    # --------------------------- ENTITY  FIELDS ------------------------------

    pets = fields.One2many(
        comodel_name='res.pet',
        inverse_name='partner',
        string='Pets',
    )

    pets_count = fields.Integer(
        string='Number of pets',
        compute='_get_pets_count',
    )

    # ----------------------- AUXILIARY FIELD METHODS -------------------------

    @api.one
    @api.depends('pets')
    def _get_pets_count(self):
        self.pets_count = len(self.pets)
