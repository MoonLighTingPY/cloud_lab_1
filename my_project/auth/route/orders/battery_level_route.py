from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import battery_level_controller
from lab4.app.my_project.auth.domain import BatteryLevel

battery_level_bp = Blueprint('battery_levels', __name__, url_prefix='/battery-levels')


@battery_level_bp.get('')
def get_all_battery_levels() -> Response:
    """
    Get all battery levels
    ---
    tags:
      - BatteryLevel
    responses:
      200:
        description: List of all battery levels
    """
    return make_response(jsonify(battery_level_controller.find_all()), HTTPStatus.OK)


@battery_level_bp.post('')
def create_battery_level() -> Response:
    """
    Create new battery level
    ---
    tags:
      - BatteryLevel
    parameters:
      - in: body
        name: battery_level
        description: Battery level data
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the battery level reading
              example: "2023-01-05 10:00:00"
            charge_level:
              type: number
              format: float
              description: Battery charge level percentage
              example: 75.00
            battery_id:
              type: integer
              description: Battery ID
              example: 1
    responses:
      201:
        description: Battery level created successfully
    """
    content = request.get_json()
    battery_level = BatteryLevel.create_from_dto(content)
    battery_level_controller.create(battery_level)
    return make_response(jsonify(battery_level.put_into_dto()), HTTPStatus.CREATED)


@battery_level_bp.get('/<int:battery_level_id>')
def get_battery_level(battery_level_id: int) -> Response:
    """
    Get battery level by ID
    ---
    tags:
      - BatteryLevel
    parameters:
      - in: path
        name: battery_level_id
        type: integer
        required: true
        description: Battery level ID
    responses:
      200:
        description: Battery level data
      404:
        description: Battery level not found
    """
    return make_response(jsonify(battery_level_controller.find_by_id(battery_level_id)), HTTPStatus.OK)


@battery_level_bp.put('/<int:battery_level_id>')
def update_battery_level(battery_level_id: int) -> Response:
    """
    Update battery level by ID
    ---
    tags:
      - BatteryLevel
    parameters:
      - in: path
        name: battery_level_id
        type: integer
        required: true
        description: Battery level ID
      - in: body
        name: battery_level
        description: Updated battery level data
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the battery level reading
              example: "2023-01-05 10:00:00"
            charge_level:
              type: number
              format: float
              description: Battery charge level percentage
              example: 75.00
            battery_id:
              type: integer
              description: Battery ID
              example: 1
    responses:
      200:
        description: Battery level updated successfully
      404:
        description: Battery level not found
    """
    content = request.get_json()
    battery_level = BatteryLevel.create_from_dto(content)
    battery_level_controller.update(battery_level_id, battery_level)
    return make_response("BatteryLevel updated", HTTPStatus.OK)


@battery_level_bp.patch('/<int:battery_level_id>')
def patch_battery_level(battery_level_id: int) -> Response:
    """
    Partially update battery level by ID
    ---
    tags:
      - BatteryLevel
    parameters:
      - in: path
        name: battery_level_id
        type: integer
        required: true
        description: Battery level ID
      - in: body
        name: battery_level
        description: Partial battery level data to update
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the battery level reading
              example: "2023-01-05 10:00:00"
            charge_level:
              type: number
              format: float
              description: Battery charge level percentage
              example: 75.00
            battery_id:
              type: integer
              description: Battery ID
              example: 1
    responses:
      200:
        description: Battery level updated successfully
      404:
        description: Battery level not found
    """
    content = request.get_json()
    battery_level_controller.patch(battery_level_id, content)
    return make_response("BatteryLevel updated", HTTPStatus.OK)


@battery_level_bp.delete('/<int:battery_level_id>')
def delete_battery_level(battery_level_id: int) -> Response:
    """
    Delete battery level by ID
    ---
    tags:
      - BatteryLevel
    parameters:
      - in: path
        name: battery_level_id
        type: integer
        required: true
        description: Battery level ID
    responses:
      200:
        description: Battery level deleted successfully
      404:
        description: Battery level not found
    """
    battery_level_controller.delete(battery_level_id)
    return make_response("BatteryLevel deleted", HTTPStatus.OK)


