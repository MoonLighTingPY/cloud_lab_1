from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import PanelAngle


class PanelAngleDAO(GeneralDAO):
    _domain_type = PanelAngle
