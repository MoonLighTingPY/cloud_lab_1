from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class PanelType(db.Model, IDto):

    __tablename__ = 'panel_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type_name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"PanelType {self.id} {self.type_name} {self.description}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'type_name': self.type_name,
            'description': self.description
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PanelType:
        obj = PanelType(**dto_dict)
        return obj
