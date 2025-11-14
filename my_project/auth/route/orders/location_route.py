from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import location_controller
from my_project.auth.domain import Location

location_bp = Blueprint('locations', __name__, url_prefix='/locations')


@location_bp.get('')
def get_all_locations() -> Response:
    """
    Get all locations
    ---
    tags:
      - Location
    responses:
      200:
        description: List of all locations
    """
    return make_response(jsonify(location_controller.find_all()), HTTPStatus.OK)


@location_bp.post('')
def create_location() -> Response:
    """
    Create new location
    ---
    tags:
      - Location
    parameters:
      - in: body
        name: location
        description: Location data
        required: true
        schema:
          type: object
          properties:
            city:
              type: string
              description: City name
              example: "Kyiv"
            street:
              type: string
              description: Street name
              example: "Shevchenka St."
    responses:
      201:
        description: Location created successfully
    """
    content = request.get_json()
    city = content['city']
    street = content['street']
    location_controller.insert_location(city, street)
    return make_response(jsonify(location_controller.find_all()), HTTPStatus.CREATED)


@location_bp.get('/<int:location_id>')
def get_location(location_id: int) -> Response:
    """
    Get location by ID
    ---
    tags:
      - Location
    parameters:
      - in: path
        name: location_id
        type: integer
        required: true
        description: Location ID
    responses:
      200:
        description: Location data
      404:
        description: Location not found
    """
    return make_response(jsonify(location_controller.find_by_id(location_id)), HTTPStatus.OK)


@location_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
    """
    Update location by ID
    ---
    tags:
      - Location
    parameters:
      - in: path
        name: location_id
        type: integer
        required: true
        description: Location ID
      - in: body
        name: location
        description: Updated location data
        required: true
        schema:
          type: object
          properties:
            city:
              type: string
              description: City name
              example: "Kyiv"
            street:
              type: string
              description: Street name
              example: "Shevchenka St."
    responses:
      200:
        description: Location updated successfully
      404:
        description: Location not found
    """
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.patch('/<int:location_id>')
def patch_location(location_id: int) -> Response:
    """
    Partially update location by ID
    ---
    tags:
      - Location
    parameters:
      - in: path
        name: location_id
        type: integer
        required: true
        description: Location ID
      - in: body
        name: location
        description: Partial location data to update
        required: true
        schema:
          type: object
          properties:
            city:
              type: string
              description: City name
              example: "Kyiv"
            street:
              type: string
              description: Street name
              example: "Shevchenka St."
    responses:
      200:
        description: Location updated successfully
      404:
        description: Location not found
    """
    content = request.get_json()
    location_controller.patch(location_id, content)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:
    """
    Delete location by ID
    ---
    tags:
      - Location
    parameters:
      - in: path
        name: location_id
        type: integer
        required: true
        description: Location ID
    responses:
      200:
        description: Location deleted successfully
      404:
        description: Location not found
    """
    location_controller.delete(location_id)
    return make_response("Client deleted", HTTPStatus.OK)
