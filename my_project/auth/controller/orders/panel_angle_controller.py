from lab4.app.my_project.auth.service import panel_angle_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PanelAngleController(GeneralController):

    _service = panel_angle_service
