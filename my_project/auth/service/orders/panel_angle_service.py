from lab4.app.my_project.auth.dao import panel_angle_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PanelAngleService(GeneralService):

    _dao = panel_angle_dao
