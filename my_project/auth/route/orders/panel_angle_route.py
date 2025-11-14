from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import panel_angle_controller
from my_project.auth.domain import PanelAngle

panel_angle_bp = Blueprint('panel_angles', __name__, url_prefix='/panel-angles')


@panel_angle_bp.get('')
def get_all_panel_angles() -> Response:
    """
    Get all panel angles
    ---
    tags:
      - PanelAngle
    responses:
      200:
        description: List of all panel angles
    """
    return make_response(jsonify(panel_angle_controller.find_all()), HTTPStatus.OK)


@panel_angle_bp.post('')
def create_panel_angle() -> Response:
    """
    Create new panel angle
    ---
    tags:
      - PanelAngle
    parameters:
      - in: body
        name: panel_angle
        description: Panel angle data
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the angle reading
              example: "2022-01-01 10:00:00"
            angle:
              type: number
              format: float
              description: Panel angle in degrees
              example: 45.00
            solar_panel_id:
              type: integer
              description: Solar panel ID
              example: 1
    responses:
      201:
        description: Panel angle created successfully
    """
    content = request.get_json()
    panel_angle = PanelAngle.create_from_dto(content)
    panel_angle_controller.create(panel_angle)
    return make_response(jsonify(panel_angle.put_into_dto()), HTTPStatus.CREATED)


@panel_angle_bp.get('/<int:panel_angle_id>')
def get_panel_angle(panel_angle_id: int) -> Response:
    """
    Get panel angle by ID
    ---
    tags:
      - PanelAngle
    parameters:
      - in: path
        name: panel_angle_id
        type: integer
        required: true
        description: Panel angle ID
    responses:
      200:
        description: Panel angle data
      404:
        description: Panel angle not found
    """
    return make_response(jsonify(panel_angle_controller.find_by_id(panel_angle_id)), HTTPStatus.OK)


@panel_angle_bp.put('/<int:panel_angle_id>')
def update_panel_angle(panel_type_id: int) -> Response:
    """
    Update panel angle by ID
    ---
    tags:
      - PanelAngle
    parameters:
      - in: path
        name: panel_angle_id
        type: integer
        required: true
        description: Panel angle ID
      - in: body
        name: panel_angle
        description: Updated panel angle data
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the angle reading
              example: "2022-01-01 10:00:00"
            angle:
              type: number
              format: float
              description: Panel angle in degrees
              example: 45.00
            solar_panel_id:
              type: integer
              description: Solar panel ID
              example: 1
    responses:
      200:
        description: Panel angle updated successfully
      404:
        description: Panel angle not found
    """
    content = request.get_json()
    panel_angle = PanelAngle.create_from_dto(content)
    panel_angle_controller.update(panel_type_id, panel_angle)
    return make_response("PanelAngle updated", HTTPStatus.OK)


@panel_angle_bp.patch('/<int:panel_angle_id>')
def patch_panel_angle(panel_angle_id: int) -> Response:
    """
    Partially update panel angle by ID
    ---
    tags:
      - PanelAngle
    parameters:
      - in: path
        name: panel_angle_id
        type: integer
        required: true
        description: Panel angle ID
      - in: body
        name: panel_angle
        description: Partial panel angle data to update
        required: true
        schema:
          type: object
          properties:
            date_time:
              type: string
              format: date-time
              description: Date and time of the angle reading
              example: "2022-01-01 10:00:00"
            angle:
              type: number
              format: float
              description: Panel angle in degrees
              example: 45.00
            solar_panel_id:
              type: integer
              description: Solar panel ID
              example: 1
    responses:
      200:
        description: Panel angle updated successfully
      404:
        description: Panel angle not found
    """
    content = request.get_json()
    panel_angle_controller.patch(panel_angle_id, content)
    return make_response("PanelAngle updated", HTTPStatus.OK)


@panel_angle_bp.delete('/<int:panel_angle_id>')
def delete_panel_types(panel_angle_id: int) -> Response:
    """
    Delete panel angle by ID
    ---
    tags:
      - PanelAngle
    parameters:
      - in: path
        name: panel_angle_id
        type: integer
        required: true
        description: Panel angle ID
    responses:
      200:
        description: Panel angle deleted successfully
      404:
        description: Panel angle not found
    """
    panel_angle_controller.delete(panel_angle_id)
    return make_response("PanelAngle deleted", HTTPStatus.OK)


