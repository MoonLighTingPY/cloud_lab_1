import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Location


class LocationDAO(GeneralDAO):
    _domain_type = Location

    def insert_location(self, city: str, street: str):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_location(:city, :street)"),
            {"city": city, "street": street}
        )
        self._session.commit()
        return result
