from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Station(db.Model, IDto):

    __tablename__ = 'station'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    total_capacity = db.Column(db.Float, nullable=False)
    installation_date = db.Column(db.Date, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref='stations')

    def __repr__(self) -> str:
        return f"Station {self.id} {self.total_capacity} {self.installation_date}, {self.location_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'total_capacity': self.total_capacity,
            'installation_date': self.installation_date,
            'location_id': self.location_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Station:
        obj = Station(**dto_dict)
        return obj
