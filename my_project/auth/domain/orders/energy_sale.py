from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EnergySale(db.Model, IDto):

    __tablename__ = 'energy_sale'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    energy_sold = db.Column(db.Float, nullable=False)
    price_per_kwh = db.Column(db.Float, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    station = db.relationship('Station', backref='energy_sales')

    def __repr__(self) -> str:
        return (f"EnergySale {self.id} {self.energy_sold} {self.price_per_kwh}, {self.date_time}, "
                f"{self.station_id}")

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'energy_sold': self.energy_sold,
            'price_per_kwh': self.price_per_kwh,
            'date_time': self.date_time,
            'station_id': self.station_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EnergySale:
        obj = EnergySale(**dto_dict)
        return obj
