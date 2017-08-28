import logging

from flask import request
from flask_restplus import Resource
from ceep_api.api.business import create_adbmonitor, update_adbmonitor, delete_adbmonitor
from ceep_api.api.serializers import adbMonitor
from ceep_api.api.restplus import api
from ceep_api.database.models import AdbMonitor


log = logging.getLogger(__name__)

ns = api.namespace('adbMonitors', description='ADB监控数据接口')


@ns.route('/')
class AdbMonitorCollection(Resource):

    @api.marshal_list_with(adbMonitor)
    def get(self):
        """
        Returns list of AdbMonitors.
        """
        adbMonitors = AdbMonitor.query.all()
        return adbMonitors

    @api.response(201, 'AdbMonitor successfully created.')
    @api.expect(adbMonitor)
    def post(self):
        """
        Creates a AdbMonitor.
        """
        data = request.json
        create_adbmonitor(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'AdbMonitor not found.')
class AdbMonitorItem(Resource):

    @api.marshal_with(adbMonitor)
    def get(self, id):
        """
        Returns a AdbMonitor.
        """
        return AdbMonitor.query.filter(AdbMonitor.id == id).one()

    @api.expect(adbMonitor)
    @api.response(204, 'AdbMonitor successfully updated.')
    def put(self, id):
        """
        Updates a AdbMonitor.
        """
        data = request.json
        update_adbmonitor(id, data)
        return None, 204

    @api.response(204, 'AdbMonitor successfully deleted.')
    def delete(self, id):
        """
        Deletes AdbMonitor.
        """
        delete_adbmonitor(id)
        return None, 204


