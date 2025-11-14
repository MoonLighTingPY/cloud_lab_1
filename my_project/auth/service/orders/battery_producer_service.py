from my_project.auth.dao import battery_producer_dao
from my_project.auth.service.general_service import GeneralService


class BatteryProducerService(GeneralService):

    _dao = battery_producer_dao

