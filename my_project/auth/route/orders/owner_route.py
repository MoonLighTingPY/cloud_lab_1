from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import owner_controller
from lab4.app.my_project.auth.domain import Owner

owner_bp = Blueprint('owners', __name__, url_prefix='/owners')


@owner_bp.get('')
def get_all_owners() -> Response:
    """
    Get all owners
    ---
    tags:
      - Owner
    responses:
      200:
        description: List of all owners
    """
    return make_response(jsonify(owner_controller.find_all()), HTTPStatus.OK)


@owner_bp.post('')
def create_owner() -> Response:
    """
    Create new owner
    ---
    tags:
      - Owner
    parameters:
      - in: body
        name: owner
        description: Owner data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Owner's first name
              example: "John"
            surname:
              type: string
              description: Owner's surname
              example: "Doe"
            contact_number:
              type: integer
              description: Contact phone number
              example: 123456789
    responses:
      201:
        description: Owner created successfully
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)


@owner_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    """
    Get owner by ID
    ---
    tags:
      - Owner
    parameters:
      - in: path
        name: owner_id
        type: integer
        required: true
        description: Owner ID
    responses:
      200:
        description: Owner data
      404:
        description: Owner not found
    """
    return make_response(jsonify(owner_controller.find_by_id(owner_id)), HTTPStatus.OK)


@owner_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    """
    Update owner by ID
    ---
    tags:
      - Owner
    parameters:
      - in: path
        name: owner_id
        type: integer
        required: true
        description: Owner ID
      - in: body
        name: owner
        description: Updated owner data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Owner's first name
              example: "John"
            surname:
              type: string
              description: Owner's surname
              example: "Doe"
            contact_number:
              type: integer
              description: Contact phone number
              example: 123456789
    responses:
      200:
        description: Owner updated successfully
      404:
        description: Owner not found
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.patch('/<int:owner_id>')
def patch_owner(owner_id: int) -> Response:
    """
    Partially update owner by ID
    ---
    tags:
      - Owner
    parameters:
      - in: path
        name: owner_id
        type: integer
        required: true
        description: Owner ID
      - in: body
        name: owner
        description: Partial owner data to update
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Owner's first name
              example: "John"
            surname:
              type: string
              description: Owner's surname
              example: "Doe"
            contact_number:
              type: integer
              description: Contact phone number
              example: 123456789
    responses:
      200:
        description: Owner updated successfully
      404:
        description: Owner not found
    """
    content = request.get_json()
    owner_controller.patch(owner_id, content)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.delete('/<int:owner_id>')
def delete_owner(owner_id: int) -> Response:
    """
    Delete owner by ID
    ---
    tags:
      - Owner
    parameters:
      - in: path
        name: owner_id
        type: integer
        required: true
        description: Owner ID
    responses:
      200:
        description: Owner deleted successfully
      404:
        description: Owner not found
    """
    owner_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)


