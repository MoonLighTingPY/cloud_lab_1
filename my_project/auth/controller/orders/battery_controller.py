from typing import List

from lab4.app.my_project.auth.service import battery_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BatteryController(GeneralController):

    _service = battery_service

    def get_batteries_after_station(self, station_id) -> List[object]:
        return self._service.get_batteries_after_station(station_id)
