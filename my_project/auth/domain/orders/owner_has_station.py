from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class OwnerHasStation(db.Model, IDto):

    __tablename__ = 'owner_has_station'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    Owner = db.relationship('Owner', backref='owners_has_stations')
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    Station = db.relationship('Station', backref='owners_has_stations')
    ownership_percentage = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"OwnerHasStation {self.id} {self.owner_id} {self.station_id}, {self.ownership_percentage}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'station_id': self.station_id,
            'ownership_percentage': self.ownership_percentage
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OwnerHasStation:
        obj = OwnerHasStation(**dto_dict)
        return obj
