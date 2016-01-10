# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from __future__ import absolute_import
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import ir
from . import workflow
from . import module
from . import res
from . import report
from . import tests

def post_init(cr, registry):
    """Rewrite ICP's to force groups"""
    from openerp import SUPERUSER_ID
    from openerp.addons.base.ir.ir_config_parameter import _default_parameters
    ICP = registry['ir.config_parameter']
    for k, func in list(_default_parameters.items()):
        v = ICP.get_param(cr, SUPERUSER_ID, k)
        _, g = func()
        ICP.set_param(cr, SUPERUSER_ID, k, v, g)
