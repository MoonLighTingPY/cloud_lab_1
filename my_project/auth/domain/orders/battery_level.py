from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class BatteryLevel(db.Model, IDto):

    __tablename__ = 'battery_level'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    charge_level = db.Column(db.Float, nullable=False)
    battery_id = db.Column(db.Integer, db.ForeignKey('battery.id'), nullable=False)
    battery = db.relationship('Battery', backref='battery_levels')

    def __repr__(self) -> str:
        return f"BatteryLevel {self.id} {self.date_time} {self.charge_level}, {self.battery_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'date_time': self.date_time,
            'charge_level': self.charge_level,
            'battery_id': self.battery_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BatteryLevel:
        obj = BatteryLevel(**dto_dict)
        return obj
