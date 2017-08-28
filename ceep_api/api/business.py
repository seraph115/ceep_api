from ceep_api.database import db
from ceep_api.database.models import AdbMonitor


def create_adbmonitor(data):
    group_id = data.get('group_id')
    device_id = data.get('device_id')
    udid = data.get('udid')

    adbMonitor = AdbMonitor(group_id, device_id, udid)    
    db.session.add(adbMonitor)
    db.session.commit


def update_adbmonitor(id, data):
    adbMonitor = AdbMonitor.query.filter(AdbMonitor.id == id).one()
    adbMonitor.group_id = data.get('group_id')
    adbMonitor.device_id = data.get('device_id')
    adbMonitor.udid = data.get('udid')

    db.session.add(adbMonitor)
    db.session.commit()


def delete_adbmonitor(id):
    adbMonitor = AdbMonitor.query.filter(AdbMonitor.id == id).one()
    db.session.delete(adbMonitor)
    db.session.commit()
