from flask_restplus import fields
from ceep_api.apis.restplus import api

adbMonitor = api.model('AdbMonitor', {
    'id': fields.Integer(readOnly=True, description='ID'),
    'group_id': fields.Integer(readOnly=True, description='Group ID'),
    'device_id': fields.Integer(readOnly=True, description='Device ID'),
    'udid': fields.String(required=True, description='UDID'),
})