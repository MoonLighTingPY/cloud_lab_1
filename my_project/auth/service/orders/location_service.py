from lab4.app.my_project.auth.dao import location_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class LocationService(GeneralService):

    _dao = location_dao

    def insert_location(self, city: str, street: str):
        self._dao.insert_location(city, street)
