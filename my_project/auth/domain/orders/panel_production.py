from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class PanelProduction(db.Model, IDto):

    __tablename__ = 'panel_production'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    production = db.Column(db.Float, nullable=False)
    solar_panel_id = db.Column(db.Integer, db.ForeignKey('solar_panel.id'), nullable=False)
    solar_panel = db.relationship('SolarPanel', backref='panel_productions')

    def __repr__(self) -> str:
        return f"PanelAngle {self.id} {self.date_time} {self.production}, {self.solar_panel_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'date_time': self.date_time,
            'production': self.production,
            'solar_panel_id': self.solar_panel_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PanelProduction:
        obj = PanelProduction(**dto_dict)
        return obj
