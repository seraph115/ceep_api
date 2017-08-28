import logging

from flask import request
from flask_restplus import Resource
from ceep_api.apis.serializers import adbMonitor
from ceep_api.apis.restplus import api
from ceep_api.database.models import AdbMonitor

log = logging.getLogger(__name__)

ns = api.namespace('adbMonitors', description='ADB监控数据接口')


@ns.route('/')
class AdbMonitorCollection(Resource):

    @api.marshal_list_with(adbMonitor)
    def get(self):
        """
        Returns list of blog categories.
        """
        adbMonitors = AdbMonitor.query.all()
        return adbMonitors
