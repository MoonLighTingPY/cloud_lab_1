from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import EnergySale


class EnergySaleDAO(GeneralDAO):
    _domain_type = EnergySale

    def get_energy_sold(self, type: str) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_energy_sold(:p1)"),
                                       {'p1': type}).mappings().all()
        return [dict(row) for row in result]
