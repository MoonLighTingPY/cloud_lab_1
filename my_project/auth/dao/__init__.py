from .orders.battery_dao import BatteryDAO
from .orders.battery_level_dao import BatteryLevelDAO
from .orders.energy_sale_dao import EnergySaleDAO
from .orders.location_dao import LocationDAO
from .orders.owner_dao import OwnerDAO
from .orders.owner_has_station_dao import OwnerHasStationDAO
from .orders.panel_angle_dao import PanelAngleDAO
from .orders.panel_production_dao import PanelProductionDAO
from .orders.panel_type_dao import PanelTypeDAO
from .orders.solar_panel_dao import SolarPanelDAO
from .orders.station_dao import StationDAO
from .orders.battery_producer_dao import BatteryProducerDAO
from .orders.battery_producer_log_dao import BatteryProducerLogDAO

battery_dao = BatteryDAO()
battery_level_dao = BatteryLevelDAO()
energy_sale_dao = EnergySaleDAO()
location_dao = LocationDAO()
owner_dao = OwnerDAO()
owner_has_station_dao = OwnerHasStationDAO()
panel_angle_dao = PanelAngleDAO()
panel_production_dao = PanelProductionDAO()
panel_type_dao = PanelTypeDAO()
solar_panel_dao = SolarPanelDAO()
station_dao = StationDAO()
battery_producer_dao = BatteryProducerDAO()
battery_producer_log_dao = BatteryProducerLogDAO()
