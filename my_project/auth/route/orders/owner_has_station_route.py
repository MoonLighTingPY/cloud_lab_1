from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import owner_has_station_controller
from my_project.auth.domain import OwnerHasStation

owner_has_station_bp = Blueprint('owner_has_stations', __name__, url_prefix='/owner-has-stations')


@owner_has_station_bp.get('')
def get_all_owner_has_stations() -> Response:
    """
    Get all owner-station relationships
    ---
    tags:
      - OwnerHasStation
    responses:
      200:
        description: List of all owner-station relationships
    """
    return make_response(jsonify(owner_has_station_controller.find_all()), HTTPStatus.OK)


@owner_has_station_bp.post('')
def create_owner_has_station() -> Response:
    """
    Create new owner-station relationship
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: body
        name: owner_has_station
        description: Owner-station relationship data
        required: true
        schema:
          type: object
          properties:
            owner_id:
              type: integer
              description: Owner ID
              example: 1
            station_id:
              type: integer
              description: Station ID
              example: 1
            ownership_percentage:
              type: number
              format: float
              description: Ownership percentage
              example: 50.00
    responses:
      200:
        description: Owner-station relationship created successfully
    """
    content = request.get_json()
    owner_id = content['owner_id']
    station_id = content['station_id']
    ownership_percentage = content['ownership_percentage']
    owner_has_station_controller.insert_owner_has_station(owner_id, station_id, ownership_percentage)
    return make_response(jsonify(owner_has_station_controller.find_all()), HTTPStatus.OK)


@owner_has_station_bp.get('/<int:owner_has_station_id>')
def get_owner_has_station(owner_has_station_id: int) -> Response:
    """
    Get owner-station relationship by ID
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: path
        name: owner_has_station_id
        type: integer
        required: true
        description: Owner-station relationship ID
    responses:
      200:
        description: Owner-station relationship data
      404:
        description: Owner-station relationship not found
    """
    return make_response(jsonify(owner_has_station_controller.find_by_id(owner_has_station_id)), HTTPStatus.OK)


@owner_has_station_bp.put('/<int:owner_has_station_id>')
def update_owner_has_station(owner_has_station_id: int) -> Response:
    """
    Update owner-station relationship by ID
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: path
        name: owner_has_station_id
        type: integer
        required: true
        description: Owner-station relationship ID
      - in: body
        name: owner_has_station
        description: Updated owner-station relationship data
        required: true
        schema:
          type: object
          properties:
            owner_id:
              type: integer
              description: Owner ID
              example: 1
            station_id:
              type: integer
              description: Station ID
              example: 1
            ownership_percentage:
              type: number
              format: float
              description: Ownership percentage
              example: 50.00
    responses:
      200:
        description: Owner-station relationship updated successfully
      404:
        description: Owner-station relationship not found
    """
    content = request.get_json()
    owner_has_station = OwnerHasStation.create_from_dto(content)
    owner_has_station_controller.update(owner_has_station_id, owner_has_station)
    return make_response("OwnerHasStation updated", HTTPStatus.OK)


@owner_has_station_bp.patch('/<int:owner_has_station_id>')
def patch_owner_has_station(owner_has_station_id: int) -> Response:
    """
    Partially update owner-station relationship by ID
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: path
        name: owner_has_station_id
        type: integer
        required: true
        description: Owner-station relationship ID
      - in: body
        name: owner_has_station
        description: Partial owner-station relationship data to update
        required: true
        schema:
          type: object
          properties:
            owner_id:
              type: integer
              description: Owner ID
              example: 1
            station_id:
              type: integer
              description: Station ID
              example: 1
            ownership_percentage:
              type: number
              format: float
              description: Ownership percentage
              example: 50.00
    responses:
      200:
        description: Owner-station relationship updated successfully
      404:
        description: Owner-station relationship not found
    """
    content = request.get_json()
    owner_has_station_controller.patch(owner_has_station_id, content)
    return make_response("OwnerHasStation updated", HTTPStatus.OK)


@owner_has_station_bp.delete('/<int:owner_has_station_id>')
def delete_owner_has_station(owner_has_station_id: int) -> Response:
    """
    Delete owner-station relationship by ID
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: path
        name: owner_has_station_id
        type: integer
        required: true
        description: Owner-station relationship ID
    responses:
      200:
        description: Owner-station relationship deleted successfully
      404:
        description: Owner-station relationship not found
    """
    owner_has_station_controller.delete(owner_has_station_id)
    return make_response("OwnerHasStation deleted", HTTPStatus.OK)


@owner_has_station_bp.get('/get-owners-after-station/<int:station_id>')
def get_owners_after_station(station_id: int) -> Response:
    """
    Get owners by station ID
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: path
        name: station_id
        type: integer
        required: true
        description: Station ID
    responses:
      200:
        description: List of owners for the specified station
    """
    return make_response(jsonify(owner_has_station_controller.get_owners_after_station(station_id)),
                         HTTPStatus.OK)


@owner_has_station_bp.get('/get-stations-after-owner/<int:owner_id>')
def get_stations_after_owner(owner_id: int) -> Response:
    """
    Get stations by owner ID
    ---
    tags:
      - OwnerHasStation
    parameters:
      - in: path
        name: owner_id
        type: integer
        required: true
        description: Owner ID
    responses:
      200:
        description: List of stations for the specified owner
    """
    return make_response(jsonify(owner_has_station_controller.get_stations_after_owner(owner_id)),
                         HTTPStatus.OK)
