from typing import List

from my_project.auth.service import energy_sale_service
from my_project.auth.controller.general_controller import GeneralController


class EnergySaleController(GeneralController):

    _service = energy_sale_service

    def get_energy_sold(self, type: str) -> List[object]:
        return self._service.get_energy_sold(type)
