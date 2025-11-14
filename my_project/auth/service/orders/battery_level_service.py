from lab4.app.my_project.auth.dao import battery_level_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BatteryLevelService(GeneralService):

    _dao = battery_level_dao
