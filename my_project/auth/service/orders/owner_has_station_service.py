from typing import List

from my_project.auth.dao import owner_has_station_dao
from my_project.auth.service.general_service import GeneralService


class OwnerHasStationService(GeneralService):

    _dao = owner_has_station_dao

    def get_owners_after_station(self, station_id) -> List[object]:
        return self._dao.get_owners_after_station(station_id)

    def get_stations_after_owner(self, owner_id) -> List[object]:
        return self._dao.get_stations_after_owner(owner_id)

    def insert_owner_has_station(self, owner_id: int, station_id: int, ownership_percentage: float):
        return self._dao.insert_owner_has_station(owner_id, station_id, ownership_percentage)
