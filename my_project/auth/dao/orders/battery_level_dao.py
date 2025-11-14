from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import BatteryLevel


class BatteryLevelDAO(GeneralDAO):
    _domain_type = BatteryLevel
