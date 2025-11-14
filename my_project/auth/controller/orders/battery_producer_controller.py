from my_project.auth.service import battery_producer_service
from my_project.auth.controller.general_controller import GeneralController


class BatteryProducerController(GeneralController):

    _service = battery_producer_service
