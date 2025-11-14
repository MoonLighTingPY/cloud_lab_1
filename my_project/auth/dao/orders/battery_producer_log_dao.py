from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import BatteryProducerLog


class BatteryProducerLogDAO(GeneralDAO):
    _domain_type = BatteryProducerLog
