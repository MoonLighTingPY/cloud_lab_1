from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import panel_type_controller
from my_project.auth.domain import PanelType

panel_type_bp = Blueprint('panel_types', __name__, url_prefix='/panel-types')


@panel_type_bp.get('')
def get_all_panel_types() -> Response:
    """
    Get all panel types
    ---
    tags:
      - PanelType
    responses:
      200:
        description: List of all panel types
    """
    return make_response(jsonify(panel_type_controller.find_all()), HTTPStatus.OK)


@panel_type_bp.post('')
def create_panel_type() -> Response:
    """
    Create new panel type
    ---
    tags:
      - PanelType
    parameters:
      - in: body
        name: panel_type
        description: Panel type data
        required: true
        schema:
          type: object
          properties:
            type_name:
              type: string
              description: Panel type name
              example: "Monocrystalline"
            description:
              type: string
              description: Panel type description
              example: "High efficiency and longevity"
    responses:
      201:
        description: Panel type created successfully
    """
    content = request.get_json()
    panel_type = PanelType.create_from_dto(content)
    panel_type_controller.create(panel_type)
    return make_response(jsonify(panel_type.put_into_dto()), HTTPStatus.CREATED)


@panel_type_bp.get('/<int:panel_type_id>')
def get_panel_type(panel_type_id: int) -> Response:
    """
    Get panel type by ID
    ---
    tags:
      - PanelType
    parameters:
      - in: path
        name: panel_type_id
        type: integer
        required: true
        description: Panel type ID
    responses:
      200:
        description: Panel type data
      404:
        description: Panel type not found
    """
    return make_response(jsonify(panel_type_controller.find_by_id(panel_type_id)), HTTPStatus.OK)


@panel_type_bp.put('/<int:panel_type_id>')
def update_panel_type(panel_type_id: int) -> Response:
    """
    Update panel type by ID
    ---
    tags:
      - PanelType
    parameters:
      - in: path
        name: panel_type_id
        type: integer
        required: true
        description: Panel type ID
      - in: body
        name: panel_type
        description: Updated panel type data
        required: true
        schema:
          type: object
          properties:
            type_name:
              type: string
              description: Panel type name
              example: "Monocrystalline"
            description:
              type: string
              description: Panel type description
              example: "High efficiency and longevity"
    responses:
      200:
        description: Panel type updated successfully
      404:
        description: Panel type not found
    """
    content = request.get_json()
    panel_type = PanelType.create_from_dto(content)
    panel_type_controller.update(panel_type_id, panel_type)
    return make_response("PanelType updated", HTTPStatus.OK)


@panel_type_bp.patch('/<int:panel_type_id>')
def patch_panel_type(panel_type_id: int) -> Response:
    """
    Partially update panel type by ID
    ---
    tags:
      - PanelType
    parameters:
      - in: path
        name: panel_type_id
        type: integer
        required: true
        description: Panel type ID
      - in: body
        name: panel_type
        description: Partial panel type data to update
        required: true
        schema:
          type: object
          properties:
            type_name:
              type: string
              description: Panel type name
              example: "Monocrystalline"
            description:
              type: string
              description: Panel type description
              example: "High efficiency and longevity"
    responses:
      200:
        description: Panel type updated successfully
      404:
        description: Panel type not found
    """
    content = request.get_json()
    panel_type_controller.patch(panel_type_id, content)
    return make_response("PanelType updated", HTTPStatus.OK)


@panel_type_bp.delete('/<int:panel_type_id>')
def delete_panel_type(panel_type_id: int) -> Response:
    """
    Delete panel type by ID
    ---
    tags:
      - PanelType
    parameters:
      - in: path
        name: panel_type_id
        type: integer
        required: true
        description: Panel type ID
    responses:
      200:
        description: Panel type deleted successfully
      404:
        description: Panel type not found
    """
    panel_type_controller.delete(panel_type_id)
    return make_response("PanelType deleted", HTTPStatus.OK)


