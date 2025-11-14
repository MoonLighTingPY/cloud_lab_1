from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import OwnerHasStation


class OwnerHasStationDAO(GeneralDAO):
    _domain_type = OwnerHasStation

    def get_owners_after_station(self, station_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_owners_after_station(:p1)"),
                                       {'p1': station_id}).mappings().all()
        return [dict(row) for row in result]

    def get_stations_after_owner(self, owner_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_stations_after_owner(:p1)"),
                                       {'p1': owner_id}).mappings().all()
        return [dict(row) for row in result]

    def insert_owner_has_station(self, owner_id: int, station_id: int, ownership_percentage: float):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_owner_has_station(:owner_id, :station_id, :ownership_percentage)"),
            {"owner_id": owner_id, "station_id": station_id, "ownership_percentage": ownership_percentage}
        )
        self._session.commit()
        return result
