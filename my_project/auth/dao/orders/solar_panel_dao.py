from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import SolarPanel


class SolarPanelDAO(GeneralDAO):
    _domain_type = SolarPanel

    def get_solar_panels_after_panel_type(self, panel_type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_solar_panels_after_panel_type(:p1)"),
                                       {'p1': panel_type_id}).mappings().all()
        return [dict(row) for row in result]

    def get_solar_panels_after_station(self, station_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_solar_panels_after_station(:p1)"),
                                       {'p1': station_id}).mappings().all()
        return [dict(row) for row in result]
