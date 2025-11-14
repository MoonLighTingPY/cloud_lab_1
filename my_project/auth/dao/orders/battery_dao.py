from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Battery


class BatteryDAO(GeneralDAO):
    _domain_type = Battery

    def get_batteries_after_station(self, station_id) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_batteries_after_station(:p1)"),
                                       {'p1': station_id}).mappings().all()
        return [dict(row) for row in result]