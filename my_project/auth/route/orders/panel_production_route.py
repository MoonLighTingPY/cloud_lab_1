from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import panel_production_controller
from lab4.app.my_project.auth.domain import PanelProduction

panel_production_bp = Blueprint('panel_productions', __name__, url_prefix='/panel-productions')


@panel_production_bp.get('')
def get_all_panel_productions() -> Response:
    """
    Get all panel productions
    ---
    tags:
      - PanelProduction
    responses:
      200:
        description: List of all panel productions
    """
    return make_response(jsonify(panel_production_controller.find_all()), HTTPStatus.OK)


@panel_production_bp.post('')
def create_panel_production() -> Response:
    """
    Create new panel production
    ---
    tags:
      - PanelProduction
    parameters:
      - in: body
        name: panel_production
        description: Panel production data
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the production reading
              example: "2022-01-01 10:00:00"
            production:
              type: number
              format: float
              description: Energy production in kWh
              example: 500.00
            solar_panel_id:
              type: integer
              description: Solar panel ID
              example: 1
    responses:
      201:
        description: Panel production created successfully
    """
    content = request.get_json()
    panel_production = PanelProduction.create_from_dto(content)
    panel_production_controller.create(panel_production)
    return make_response(jsonify(panel_production.put_into_dto()), HTTPStatus.CREATED)


@panel_production_bp.get('/<int:panel_production_id>')
def get_panel_production(panel_production_id: int) -> Response:
    """
    Get panel production by ID
    ---
    tags:
      - PanelProduction
    parameters:
      - in: path
        name: panel_production_id
        type: integer
        required: true
        description: Panel production ID
    responses:
      200:
        description: Panel production data
      404:
        description: Panel production not found
    """
    return make_response(jsonify(panel_production_controller.find_by_id(panel_production_id)), HTTPStatus.OK)


@panel_production_bp.put('/<int:panel_production_id>')
def update_panel_production(panel_production_id: int) -> Response:
    """
    Update panel production by ID
    ---
    tags:
      - PanelProduction
    parameters:
      - in: path
        name: panel_production_id
        type: integer
        required: true
        description: Panel production ID
      - in: body
        name: panel_production
        description: Updated panel production data
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the production reading
              example: "2022-01-01 10:00:00"
            production:
              type: number
              format: float
              description: Energy production in kWh
              example: 500.00
            solar_panel_id:
              type: integer
              description: Solar panel ID
              example: 1
    responses:
      200:
        description: Panel production updated successfully
      404:
        description: Panel production not found
    """
    content = request.get_json()
    panel_production = PanelProduction.create_from_dto(content)
    panel_production_controller.update(panel_production_id, panel_production)
    return make_response("PanelProduction updated", HTTPStatus.OK)


@panel_production_bp.patch('/<int:panel_production_id>')
def patch_panel_production(panel_production_id: int) -> Response:
    """
    Partially update panel production by ID
    ---
    tags:
      - PanelProduction
    parameters:
      - in: path
        name: panel_production_id
        type: integer
        required: true
        description: Panel production ID
      - in: body
        name: panel_production
        description: Partial panel production data to update
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the production reading
              example: "2022-01-01 10:00:00"
            production:
              type: number
              format: float
              description: Energy production in kWh
              example: 500.00
            solar_panel_id:
              type: integer
              description: Solar panel ID
              example: 1
    responses:
      200:
        description: Panel production updated successfully
      404:
        description: Panel production not found
    """
    content = request.get_json()
    panel_production_controller.patch(panel_production_id, content)
    return make_response("PanelProduction updated", HTTPStatus.OK)


@panel_production_bp.delete('/<int:panel_production_id>')
def delete_panel_types(panel_production_id: int) -> Response:
    """
    Delete panel production by ID
    ---
    tags:
      - PanelProduction
    parameters:
      - in: path
        name: panel_production_id
        type: integer
        required: true
        description: Panel production ID
    responses:
      200:
        description: Panel production deleted successfully
      404:
        description: Panel production not found
    """
    panel_production_controller.delete(panel_production_id)
    return make_response("PanelProduction deleted", HTTPStatus.OK)


