from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import station_controller
from lab4.app.my_project.auth.domain import Station

station_bp = Blueprint('stations', __name__, url_prefix='/stations')


@station_bp.get('')
def get_all_stations() -> Response:
    """
    Get all stations
    ---
    tags:
      - Station
    responses:
      200:
        description: List of all stations
    """
    return make_response(jsonify(station_controller.find_all()), HTTPStatus.OK)


@station_bp.post('')
def create_station() -> Response:
    """
    Create new station
    ---
    tags:
      - Station
    parameters:
      - in: body
        name: station
        description: Station data
        required: true
        schema:
          type: object
          properties:
            total_capacity:
              type: number
              format: float
              description: Total capacity in kW
              example: 5000.00
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-15"
            location_id:
              type: integer
              description: Location ID
              example: 1
    responses:
      201:
        description: Station created successfully
    """
    content = request.get_json()
    station = Station.create_from_dto(content)
    station_controller.create(station)
    return make_response(jsonify(station.put_into_dto()), HTTPStatus.CREATED)


@station_bp.get('/<int:station_id>')
def get_station(station_id: int) -> Response:
    """
    Get station by ID
    ---
    tags:
      - Station
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
    responses:
      200:
        description: Station data
      404:
        description: Station not found
    """
    return make_response(jsonify(station_controller.find_by_id(station_id)), HTTPStatus.OK)


@station_bp.put('/<int:station_id>')
def update_station(station_id: int) -> Response:
    """
    Update station by ID
    ---
    tags:
      - Station
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
      - in: body
        name: station
        description: Updated station data
        required: true
        schema:
          type: object
          properties:
            total_capacity:
              type: number
              format: float
              description: Total capacity in kW
              example: 5000.00
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-15"
            location_id:
              type: integer
              description: Location ID
              example: 1
    responses:
      200:
        description: Station updated successfully
      404:
        description: Station not found
    """
    content = request.get_json()
    station = Station.create_from_dto(content)
    station_controller.update(station_id, station)
    return make_response("Station updated", HTTPStatus.OK)


@station_bp.patch('/<int:station_id>')
def patch_station(station_id: int) -> Response:
    """
    Partially update station by ID
    ---
    tags:
      - Station
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
      - in: body
        name: station
        description: Partial station data to update
        required: true
        schema:
          type: object
          properties:
            total_capacity:
              type: number
              format: float
              description: Total capacity in kW
              example: 5000.00
            installation_date:
              type: string
              format: date
              description: Installation date
              example: "2022-01-15"
            location_id:
              type: integer
              description: Location ID
              example: 1
    responses:
      200:
        description: Station updated successfully
      404:
        description: Station not found
    """
    content = request.get_json()
    station_controller.patch(station_id, content)
    return make_response("Station updated", HTTPStatus.OK)


@station_bp.delete('/<int:station_id>')
def delete_station(station_id: int) -> Response:
    """
    Delete station by ID
    ---
    tags:
      - Station
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
    responses:
      200:
        description: Station deleted successfully
      404:
        description: Station not found
    """
    station_controller.delete(station_id)
    return make_response("Station deleted", HTTPStatus.OK)


