from past.builtins import basestring
from builtins import object
import openerp.sql_db

class Session(object):
    def __init__(self, cr, uid):
        assert isinstance(cr, openerp.sql_db.Cursor)
        assert isinstance(uid, (int, int))
        self.cr = cr
        self.uid = uid

class Record(object):
    def __init__(self, model, record_id):
        assert isinstance(model, basestring)
        assert isinstance(record_id, (int, int))
        self.model = model
        self.id = record_id

class WorkflowActivity(object):
    KIND_FUNCTION = 'function'
    KIND_DUMMY = 'dummy'
    KIND_STOPALL = 'stopall'
    KIND_SUBFLOW = 'subflow'
