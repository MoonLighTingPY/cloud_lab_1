from my_project.auth.dao import station_dao
from my_project.auth.service.general_service import GeneralService


class StationService(GeneralService):

    _dao = station_dao
