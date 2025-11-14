from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.battery_route import battery_bp
    from .orders.battery_level_route import battery_level_bp
    from .orders.energy_sale_route import energy_sale_bp
    from .orders.location_route import location_bp
    from .orders.owner_has_station_route import owner_has_station_bp
    from .orders.owner_route import owner_bp
    from .orders.panel_angle_route import panel_angle_bp
    from .orders.panel_production_route import panel_production_bp
    from .orders.panel_type_route import panel_type_bp
    from .orders.solar_panel_route import solar_panel_bp
    from .orders.station_route import station_bp

    app.register_blueprint(battery_bp)
    app.register_blueprint(battery_level_bp)
    app.register_blueprint(energy_sale_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(owner_has_station_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(panel_angle_bp)
    app.register_blueprint(panel_production_bp)
    app.register_blueprint(panel_type_bp)
    app.register_blueprint(solar_panel_bp)
    app.register_blueprint(station_bp)
