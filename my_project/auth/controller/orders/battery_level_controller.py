from typing import List

from lab4.app.my_project.auth.service import battery_level_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BatteryLevelController(GeneralController):

    _service = battery_level_service
