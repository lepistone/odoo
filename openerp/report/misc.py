# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from __future__ import print_function
from __future__ import division
from builtins import range
from past.utils import old_div
from pychart import *

colorline = [color.T(r=old_div(((r+3) % 11),10.0),
                     g=old_div(((g+6) % 11),10.0),
                     b=old_div(((b+9) % 11),10.0))
             for r in range(11) for g in range(11) for b in range(11)]

def choice_colors(n):
    if n:
        return colorline[0:-1:old_div(len(colorline),n)]
    return []

if __name__=='__main__':
    print(choice_colors(10))
