from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import battery_controller
from my_project.auth.domain import Battery

battery_bp = Blueprint('batteries', __name__, url_prefix='/batteries')


@battery_bp.get('')
def get_all_batteries() -> Response:
    """
    Get all batteries
    ---
    tags:
      - Battery
    responses:
      200:
        description: List of all batteries
    """
    return make_response(jsonify(battery_controller.find_all()), HTTPStatus.OK)


@battery_bp.post('')
def create_battery() -> Response:
    """
    Create new battery
    ---
    tags:
      - Battery
    parameters:
      - in: body
        name: battery
        description: Battery data
        required: true
        schema:
          type: object
          properties:
            capacity:
              type: string
              description: Battery capacity
              example: "1000"
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-05"
            station_id:
              type: integer
              description: Station ID
              example: 1
    responses:
      201:
        description: Battery created successfully
    """
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.create(battery)
    return make_response(jsonify(battery.put_into_dto()), HTTPStatus.CREATED)


@battery_bp.get('/<int:battery_id>')
def get_battery(battery_id: int) -> Response:
    """
    Get battery by ID
    ---
    tags:
      - Battery
    parameters:
      - in: path
        name: battery_id
        type: integer
        required: true
        description: Battery ID
    responses:
      200:
        description: Battery data
      404:
        description: Battery not found
    """
    return make_response(jsonify(battery_controller.find_by_id(battery_id)), HTTPStatus.OK)


@battery_bp.put('/<int:battery_id>')
def update_battery(battery_id: int) -> Response:
    """
    Update battery by ID
    ---
    tags:
      - Battery
    parameters:
      - in: path
        name: battery_id
        type: integer
        required: true
        description: Battery ID
      - in: body
        name: battery
        description: Updated battery data
        required: true
        schema:
          type: object
          properties:
            capacity:
              type: string
              description: Battery capacity
              example: "1000"
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-05"
            station_id:
              type: integer
              description: Station ID
              example: 1
    responses:
      200:
        description: Battery updated successfully
      404:
        description: Battery not found
    """
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.update(battery_id, battery)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.patch('/<int:battery_id>')
def patch_battery(battery_id: int) -> Response:
    """
    Partially update battery by ID
    ---
    tags:
      - Battery
    parameters:
      - in: path
        name: battery_id
        type: integer
        required: true
        description: Battery ID
      - in: body
        name: battery
        description: Partial battery data to update
        required: true
        schema:
          type: object
          properties:
            capacity:
              type: string
              description: Battery capacity
              example: "1000"
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-05"
            station_id:
              type: integer
              description: Station ID
              example: 1
    responses:
      200:
        description: Battery updated successfully
      404:
        description: Battery not found
    """
    content = request.get_json()
    battery_controller.patch(battery_id, content)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.delete('/<int:battery_id>')
def delete_battery(battery_id: int) -> Response:
    """
    Delete battery by ID
    ---
    tags:
      - Battery
    parameters:
      - in: path
        name: battery_id
        type: integer
        required: true
        description: Battery ID
    responses:
      200:
        description: Battery deleted successfully
      404:
        description: Battery not found
    """
    battery_controller.delete(battery_id)
    return make_response("Battery deleted", HTTPStatus.OK)


@battery_bp.get('/get-batteries-after-station/<int:station_id>')
def get_batteries_after_station(station_id: int) -> Response:
    """
    Get batteries by station ID
    ---
    tags:
      - Battery
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
    responses:
      200:
        description: List of batteries for the specified station
    """
    return make_response(jsonify(battery_controller.get_batteries_after_station(station_id)), HTTPStatus.OK)

