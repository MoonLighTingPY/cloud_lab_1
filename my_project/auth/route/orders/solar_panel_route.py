from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import solar_panel_controller
from lab4.app.my_project.auth.domain import SolarPanel

solar_panel_bp = Blueprint('solar_panels', __name__, url_prefix='/solar-panels')


@solar_panel_bp.get('')
def get_all_solar_panels() -> Response:
    """
    Get all solar panels
    ---
    tags:
      - SolarPanel
    responses:
      200:
        description: List of all solar panels
    """
    return make_response(jsonify(solar_panel_controller.find_all()), HTTPStatus.OK)


@solar_panel_bp.post('')
def create_solar_panel() -> Response:
    """
    Create new solar panel
    ---
    tags:
      - SolarPanel
    parameters:
      - in: body
        name: solar_panel
        description: Solar panel data
        required: true
        schema:
          type: object
          properties:
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-01"
            panel_type_id:
              type: integer
              description: Panel type ID
              example: 3
            station_id:
              type: integer
              description: Station ID
              example: 7
    responses:
      201:
        description: Solar panel created successfully
    """
    content = request.get_json()
    solar_panel = SolarPanel.create_from_dto(content)
    solar_panel_controller.create(solar_panel)
    return make_response(jsonify(solar_panel.put_into_dto()), HTTPStatus.CREATED)


@solar_panel_bp.get('/<int:solar_panel_id>')
def get_solar_panel(solar_panel_id: int) -> Response:
    """
    Get solar panel by ID
    ---
    tags:
      - SolarPanel
    parameters:
      - in: path
        name: solar_panel_id
        type: integer
        required: true
        description: Solar panel ID
    responses:
      200:
        description: Solar panel data
      404:
        description: Solar panel not found
    """
    return make_response(jsonify(solar_panel_controller.find_by_id(solar_panel_id)), HTTPStatus.OK)


@solar_panel_bp.put('/<int:solar_panel_id>')
def update_solar_panel(solar_panel_id: int) -> Response:
    """
    Update solar panel by ID
    ---
    tags:
      - SolarPanel
    parameters:
      - in: path
        name: solar_panel_id
        type: integer
        required: true
        description: Solar panel ID
      - in: body
        name: solar_panel
        description: Updated solar panel data
        required: true
        schema:
          type: object
          properties:
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-01"
            panel_type_id:
              type: integer
              description: Panel type ID
              example: 3
            station_id:
              type: integer
              description: Station ID
              example: 7
    responses:
      200:
        description: Solar panel updated successfully
      404:
        description: Solar panel not found
    """
    content = request.get_json()
    solar_panel = SolarPanel.create_from_dto(content)
    solar_panel_controller.update(solar_panel_id, solar_panel)
    return make_response("SolarPanel updated", HTTPStatus.OK)


@solar_panel_bp.patch('/<int:solar_panel_id>')
def patch_solar_panel(solar_panel_id: int) -> Response:
    """
    Partially update solar panel by ID
    ---
    tags:
      - SolarPanel
    parameters:
      - in: path
        name: solar_panel_id
        type: integer
        required: true
        description: Solar panel ID
      - in: body
        name: solar_panel
        description: Partial solar panel data to update
        required: true
        schema:
          type: object
          properties:
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-01"
            panel_type_id:
              type: integer
              description: Panel type ID
              example: 3
            station_id:
              type: integer
              description: Station ID
              example: 7
    responses:
      200:
        description: Solar panel updated successfully
      404:
        description: Solar panel not found
    """
    content = request.get_json()
    solar_panel_controller.patch(solar_panel_id, content)
    return make_response("SolarPanel updated", HTTPStatus.OK)


@solar_panel_bp.delete('/<int:solar_panel_id>')
def delete_solar_panel(solar_panel_id: int) -> Response:
    """
    Delete solar panel by ID
    ---
    tags:
      - SolarPanel
    parameters:
      - in: path
        name: solar_panel_id
        type: integer
        required: true
        description: Solar panel ID
    responses:
      200:
        description: Solar panel deleted successfully
      404:
        description: Solar panel not found
    """
    solar_panel_controller.delete(solar_panel_id)
    return make_response("SolarPanel deleted", HTTPStatus.OK)


@solar_panel_bp.get('/get-solar-panels-after-panel-type/<int:panel_type_id>')
def get_solar_panels_after_panel_type(panel_type_id: int) -> Response:
    """
    Get solar panels by panel type ID
    ---
    tags:
      - SolarPanel
    parameters:
      - in: path
        name: panel_type_id
        type: integer
        required: true
        description: Panel type ID
    responses:
      200:
        description: List of solar panels for the specified panel type
    """
    return make_response(jsonify(solar_panel_controller.get_solar_panels_after_panel_type(panel_type_id)),
                         HTTPStatus.OK)

@solar_panel_bp.get('/get-solar-panels-after-station/<int:station_id>')
def get_solar_panels_after_station(station_id: int) -> Response:
    """
    Get solar panels by station ID
    ---
    tags:
      - SolarPanel
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
    responses:
      200:
        description: List of solar panels for the specified station
    """
    return make_response(jsonify(solar_panel_controller.get_solar_panels_after_station(station_id)), HTTPStatus.OK)

