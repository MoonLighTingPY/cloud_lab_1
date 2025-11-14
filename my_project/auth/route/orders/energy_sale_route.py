from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import energy_sale_controller
from my_project.auth.domain import EnergySale

energy_sale_bp = Blueprint('energy_sales', __name__, url_prefix='/energy-sales')


@energy_sale_bp.get('')
def get_all_energy_sales() -> Response:
    """
    Get all energy sales
    ---
    tags:
      - EnergySale
    responses:
      200:
        description: List of all energy sales
    """
    return make_response(jsonify(energy_sale_controller.find_all()), HTTPStatus.OK)


@energy_sale_bp.post('')
def create_energy_sale() -> Response:
    """
    Create new energy sale
    ---
    tags:
      - EnergySale
    parameters:
      - in: body
        name: energy_sale
        description: Energy sale data
        required: true
        schema:
          type: object
          properties:
            energy_sold:
              type: number
              format: float
              description: Amount of energy sold in kWh
              example: 100.50
            price_per_kwh:
              type: number
              format: float
              description: Price per kWh
              example: 0.15
            date_time:
              type: string
              format: date-time
              description: Date and time of the sale
              example: "2023-01-01 10:00:00"
            station_id:
              type: integer
              description: Station ID
              example: 1
    responses:
      201:
        description: Energy sale created successfully
    """
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.create(energy_sale)
    return make_response(jsonify(energy_sale.put_into_dto()), HTTPStatus.CREATED)


@energy_sale_bp.get('/<int:energy_sale_id>')
def get_energy_sale(energy_sale_id: int) -> Response:
    """
    Get energy sale by ID
    ---
    tags:
      - EnergySale
    parameters:
      - in: path
        name: energy_sale_id
        type: integer
        required: true
        description: Energy sale ID
    responses:
      200:
        description: Energy sale data
      404:
        description: Energy sale not found
    """
    return make_response(jsonify(energy_sale_controller.find_by_id(energy_sale_id)), HTTPStatus.OK)


@energy_sale_bp.put('/<int:energy_sale_id>')
def update_energy_sale(energy_sale_id: int) -> Response:
    """
    Update energy sale by ID
    ---
    tags:
      - EnergySale
    parameters:
      - in: path
        name: energy_sale_id
        type: integer
        required: true
        description: Energy sale ID
      - in: body
        name: energy_sale
        description: Updated energy sale data
        required: true
        schema:
          type: object
          properties:
            energy_sold:
              type: number
              format: float
              description: Amount of energy sold in kWh
              example: 100.50
            price_per_kwh:
              type: number
              format: float
              description: Price per kWh
              example: 0.15
            date_time:
              type: string
              format: date-time
              description: Date and time of the sale
              example: "2023-01-01 10:00:00"
            station_id:
              type: integer
              description: Station ID
              example: 1
    responses:
      200:
        description: Energy sale updated successfully
      404:
        description: Energy sale not found
    """
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.update(energy_sale_id, energy_sale)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.patch('/<int:energy_sale_id>')
def patch_energy_sale(energy_sale_id: int) -> Response:
    """
    Partially update energy sale by ID
    ---
    tags:
      - EnergySale
    parameters:
      - in: path
        name: energy_sale_id
        type: integer
        required: true
        description: Energy sale ID
      - in: body
        name: energy_sale
        description: Partial energy sale data to update
        required: true
        schema:
          type: object
          properties:
            energy_sold:
              type: number
              format: float
              description: Amount of energy sold in kWh
              example: 100.50
            price_per_kwh:
              type: number
              format: float
              description: Price per kWh
              example: 0.15
            date_time:
              type: string
              format: date-time
              description: Date and time of the sale
              example: "2023-01-01 10:00:00"
            station_id:
              type: integer
              description: Station ID
              example: 1
    responses:
      200:
        description: Energy sale updated successfully
      404:
        description: Energy sale not found
    """
    content = request.get_json()
    energy_sale_controller.patch(energy_sale_id, content)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.delete('/<int:energy_sale_id>')
def delete_energy_sale(energy_sale_id: int) -> Response:
    """
    Delete energy sale by ID
    ---
    tags:
      - EnergySale
    parameters:
      - in: path
        name: energy_sale_id
        type: integer
        required: true
        description: Energy sale ID
    responses:
      200:
        description: Energy sale deleted successfully
      404:
        description: Energy sale not found
    """
    energy_sale_controller.delete(energy_sale_id)
    return make_response("EnergySale deleted", HTTPStatus.OK)


@energy_sale_bp.get('/calculate-energy-sold/<string:type>')
def get_energy_sold(type: str) -> Response:
    """
    Calculate total energy sold by type
    ---
    tags:
      - EnergySale
    parameters:
      - in: path
        name: type
        type: string
        required: true
        description: Calculation type (e.g., 'daily', 'monthly', 'yearly')
    responses:
      200:
        description: Calculated energy sold data
    """
    return make_response(jsonify(energy_sale_controller.get_energy_sold(type)), HTTPStatus.OK)