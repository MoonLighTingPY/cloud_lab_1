from lab4.app.my_project.auth.dao import panel_type_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PanelTypeService(GeneralService):

    _dao = panel_type_dao
