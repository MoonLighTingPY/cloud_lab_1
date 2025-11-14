from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Battery(db.Model, IDto):

    __tablename__ = 'battery'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    capacity = db.Column(db.String(45), nullable=False)
    installation_date = db.Column(db.Date, nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    station = db.relationship('Station', backref='batteries')

    def __repr__(self) -> str:
        return f"Battery {self.id} {self.capacity} {self.installation_date}, {self.station_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'capacity': self.capacity,
            'installation_date': self.installation_date,
            'station_id': self.station_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Battery:
        obj = Battery(**dto_dict)
        return obj
