from typing import List

from lab4.app.my_project.auth.service import solar_panel_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class SolarPanelController(GeneralController):

    _service = solar_panel_service

    def get_solar_panels_after_panel_type(self, panel_type_id) -> List[object]:
        return self._service.get_solar_panels_after_panel_type(panel_type_id)

    def get_solar_panels_after_station(self, station_id) -> List[object]:
        return self._service.get_solar_panels_after_station(station_id)
