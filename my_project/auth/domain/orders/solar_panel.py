from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class SolarPanel(db.Model, IDto):

    __tablename__ = 'solar_panel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    installation_date = db.Column(db.Date, nullable=False)
    panel_type_id = db.Column(db.Integer, db.ForeignKey('panel_type.id'), nullable=False)
    panel_type = db.relationship('PanelType', backref='panels')
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    station = db.relationship('Station', backref='panels')

    def __repr__(self) -> str:
        return f"SolarPanel {self.id} {self.installation_date} {self.panel_type_id}, {self.station_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'installation_date': self.installation_date,
            'panel_type_id': self.panel_type_id,
            'station_id': self.station_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SolarPanel:
        obj = SolarPanel(**dto_dict)
        return obj
