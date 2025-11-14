from lab4.app.my_project.auth.service import panel_production_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PanelProductionController(GeneralController):

    _service = panel_production_service
