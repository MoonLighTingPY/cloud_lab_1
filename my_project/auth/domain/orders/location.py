from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Location(db.Model, IDto):

    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    city = db.Column(db.String(45), nullable=False)
    street = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Location {self.id} {self.city} {self.street}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'city': self.city,
            'street': self.street
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Location:
        obj = Location(**dto_dict)
        return obj
