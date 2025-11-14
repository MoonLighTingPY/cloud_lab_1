from typing import List

from my_project.auth.dao import battery_dao
from my_project.auth.service.general_service import GeneralService


class BatteryService(GeneralService):

    _dao = battery_dao

    def get_batteries_after_station(self, station_id) -> List[object]:
        return self._dao.get_batteries_after_station(station_id)
