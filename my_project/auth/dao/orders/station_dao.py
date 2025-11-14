from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Station


class StationDAO(GeneralDAO):
    _domain_type = Station

