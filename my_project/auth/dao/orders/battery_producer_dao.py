from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import BatteryProducer


class BatteryProducerDAO(GeneralDAO):
    _domain_type = BatteryProducer
