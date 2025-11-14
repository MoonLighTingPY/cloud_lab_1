from .orders.battery_controller import BatteryController
from .orders.battery_level_controller import BatteryLevelController
from .orders.energy_sale_controller import EnergySaleController
from .orders.location_controller import LocationController
from .orders.owner_controller import OwnerController
from .orders.owner_has_station_controller import OwnerHasStationController
from .orders.panel_angle_controller import PanelAngleController
from .orders.panel_production_controller import PanelProductionController
from .orders.panel_type_controller import PanelTypeController
from .orders.solar_panel_controller import SolarPanelController
from .orders.station_controller import StationController
from .orders.battery_producer_controller import BatteryProducerController
from .orders.battery_producer_log_controller import BatteryProducerLogController

battery_controller = BatteryController()
battery_level_controller = BatteryLevelController()
energy_sale_controller = EnergySaleController()
location_controller = LocationController()
owner_controller = OwnerController()
owner_has_station_controller = OwnerHasStationController()
panel_angle_controller = PanelAngleController()
panel_production_controller = PanelProductionController()
panel_type_controller = PanelTypeController()
solar_panel_controller = SolarPanelController()
station_controller = StationController()
battery_producer_controller = BatteryProducerController()
battery_producer_log_controller = BatteryProducerLogController()
