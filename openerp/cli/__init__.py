from __future__ import absolute_import
import logging
import sys
import os

import openerp

from .command import Command, main

from . import deploy
from . import scaffold
from . import server
from . import shell
from . import start
