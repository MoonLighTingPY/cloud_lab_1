from my_project.auth.service import owner_service
from my_project.auth.controller.general_controller import GeneralController


class OwnerController(GeneralController):

    _service = owner_service
