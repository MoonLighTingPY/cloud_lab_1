from typing import List

from lab4.app.my_project.auth.dao import solar_panel_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class SolarPanelService(GeneralService):

    _dao = solar_panel_dao

    def get_solar_panels_after_panel_type(self, panel_type_id) -> List[object]:
        return self._dao.get_solar_panels_after_panel_type(panel_type_id)

    def get_solar_panels_after_station(self, station_id) -> List[object]:
        return self._dao.get_solar_panels_after_station(station_id)
