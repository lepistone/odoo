# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from __future__ import absolute_import
import openerp

from . import interface
from . import print_xml
from . import print_fnc
from . import custom
from . import render
from . import int_to_text

from . import report_sxw

from . import printscreen

def render_report(cr, uid, ids, name, data, context=None):
    """
    Helper to call ``ir.actions.report.xml.render_report()``.
    """
    registry = openerp.modules.registry.RegistryManager.get(cr.dbname)
    return registry['ir.actions.report.xml'].render_report(cr, uid, ids, name, data, context)
