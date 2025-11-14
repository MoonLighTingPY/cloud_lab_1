from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class BatteryProducer(db.Model, IDto):

    __tablename__ = 'battery_producer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    battery_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Battery {self.id} {self.battery_id} {self.name}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            "battery_id": self.battery_id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BatteryProducer:
        obj = BatteryProducer(**dto_dict)
        return obj
