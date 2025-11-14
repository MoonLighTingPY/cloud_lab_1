from .orders.battery_service import BatteryService
from .orders.battery_level_service import BatteryLevelService
from .orders.energy_sale_service import EnergySaleService
from .orders.location_service import LocationService
from .orders.owner_has_station_service import OwnerHasStationService
from .orders.owner_service import OwnerService
from .orders.panel_angle_service import PanelAngleService
from .orders.panel_production_service import PanelProductionService
from .orders.panel_type_service import PanelTypeService
from .orders.solar_panel_service import SolarPanelService
from .orders.station_service import StationService
from .orders.battery_producer_service import BatteryProducerService
from .orders.battery_producer_log_service import BatteryProducerLogService

battery_service = BatteryService()
battery_level_service = BatteryLevelService()
energy_sale_service = EnergySaleService()
location_service = LocationService()
owner_has_station_service = OwnerHasStationService()
owner_service = OwnerService()
panel_angle_service = PanelAngleService()
panel_production_service = PanelProductionService()
panel_type_service = PanelTypeService()
solar_panel_service = SolarPanelService()
station_service = StationService()
battery_producer_service = BatteryProducerService()
battery_producer_log_service = BatteryProducerLogService()
