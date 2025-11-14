from lab4.app.my_project.auth.dao import owner_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class OwnerService(GeneralService):

    _dao = owner_dao
