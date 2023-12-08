
from flask import Blueprint, jsonify, request
from api.roles.utils import format_roles, update_roles 
from api.roles.utils import get_roles, validate_roles
from api.roles.utils import (
create_roles, get_roles, get_roles, validate_roles
)
from api.roles.validate_roles import rolesCreate, rolesUpdate
api_roles = Blueprint("Api roles", __name__, url_prefix="/api/roles")

@api_roles.route("/", methods=["GET"])
def get__roles():
    """
    Get all roles
    """
    data_roles = get_roles()
    return {
		"message": " roles consulta exitosamente",
        "status": 1,
        "data": data_roles,
    }

@api_roles.route("/", methods=["POST"])
def create__roles():
    """
    Create roles
    """
    try:
        roles_validate = rolesCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_roles = validate_roles(roles_validate.id_rol)
    if data_roles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_roles = create_roles(roles_validate.dict(exclude_unset=True))
    return {
				"message": "roles creada exitosamente",
				"status": 1,
				"data": {
                    "id_rol": int(data_roles.id_rol),
                }
				
			}

@api_roles.route("/", methods=["PUT"])
def update__roles():
    """
    Create roles
    """
    try:
        roles_validate = rolesUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_roles = validate_roles(int(roles_validate.id_rol))
    if not data_roles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    roles_update = roles_validate.dict(exclude_unset=True)
    if not roles_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_roles = update_roles(int(roles_validate.id_rol), roles_update)
    return {
       
        "message": "roles actualizado exitosamente",
        "status": 1,
        "data": data_roles,
    }



@api_roles.route("/<int:id_rol>", methods=["GET"]) 
def get_only_roles(id_rol: str):
    """
    Create roles
    """
    roles = validate_roles(id_rol)
    if not roles:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    
    data_roles= format_roles(roles)
    return {
        "message": "roles consulta exitosamente",
        "status": 1,
        "data": data_roles,
    }
