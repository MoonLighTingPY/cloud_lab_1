from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class BatteryProducerLog(db.Model, IDto):

    __tablename__ = 'battery_producer_log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    battery_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"Battery {self.id} {self.battery_id} {self.name}, {self.deleted_at}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            "battery_id": self.battery_id,
            "name": self.name,
            "deleted_at": self.deleted_at
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BatteryProducerLog:
        obj = BatteryProducerLog(**dto_dict)
        return obj
