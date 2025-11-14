from my_project.auth.service import location_service
from my_project.auth.controller.general_controller import GeneralController


class LocationController(GeneralController):

    _service = location_service

    def insert_location(self, city: str, street: str):
        self._service.insert_location(city, street)