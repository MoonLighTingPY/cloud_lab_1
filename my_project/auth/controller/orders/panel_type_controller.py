from my_project.auth.service import panel_type_service
from my_project.auth.controller.general_controller import GeneralController


class PanelTypeController(GeneralController):

    _service = panel_type_service
