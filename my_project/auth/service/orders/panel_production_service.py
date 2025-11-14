from my_project.auth.dao import panel_production_dao
from my_project.auth.service.general_service import GeneralService


class PanelProductionService(GeneralService):

    _dao = panel_production_dao
