from lab4.app.my_project.auth.dao import station_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class StationService(GeneralService):

    _dao = station_dao
