from datetime import datetime
from ceep_api.database import db

class AdbMonitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, unique=False, nullable=False)
    device_id = db.Column(db.Integer, unique=True, nullable=False)
    udid = db.Column(db.String(25), unique=True, nullable=False)

    def __init__(self, udid):
        self.udid = udid

    def __repr__(self):
        return '<AdbMonitor %r>' % self.udid

        