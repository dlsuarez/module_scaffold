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
#   model.new                                                                 #
###############################################################################

class ModelNew(models.Model):

    _name = 'res.pet'
    _description = _('Description of model new.')
    _order = "id desc"

    # --------------------------- ENTITY  FIELDS ------------------------------

    name = fields.Char(
        string='Name',
    )

    partner = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        domain=[('customer', '=', True)],
        readonly=False,
        required=True,
    )
