from typing import List

from my_project.auth.dao import energy_sale_dao
from my_project.auth.service.general_service import GeneralService


class EnergySaleService(GeneralService):

    _dao = energy_sale_dao

    def get_energy_sold(self, type: str) -> List[object]:
        return self._dao.get_energy_sold(type)
