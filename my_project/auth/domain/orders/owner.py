from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Owner(db.Model, IDto):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Owner {self.id} {self.name} {self.surname}, {self.contact_number}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'contact_number': self.contact_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owner:
        obj = Owner(**dto_dict)
        return obj
