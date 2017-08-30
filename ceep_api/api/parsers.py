from flask_restplus import reqparse

adbmonitor_arguments = reqparse.RequestParser()
adbmonitor_arguments.add_argument('id', type=int, required=False, default=0, help='ID')
adbmonitor_arguments.add_argument('group_id', type=int, required=False, default=0, help='Group ID')
adbmonitor_arguments.add_argument('device_id', type=int, required=False, default=0, help='Device ID')
adbmonitor_arguments.add_argument('udid', type=str, required=False, help='UDID')
