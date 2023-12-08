from flask import Blueprint, jsonify, request 
from api.permisos.utils import get_permisos, validate_permisos , format_permisos,update_permisos, validate_permisos 
from api.permisos.utils import (
create_permisos, get_permisos, get_permisos, validate_permisos
)
from api.permisos.validate_permisos import permisosCreate, permisosUpdate
api_permisos = Blueprint("Api permisos", __name__, url_prefix="/api/permisos")

@api_permisos.route("/", methods=["GET"])
def getall_permisos():
    """
    Get all permisos
    """
    data_permisos = get_permisos()
    return {
		"message": " permisos consulta exitosamente",
        "status": 1,
        "data": data_permisos,
    }

@api_permisos.route("/", methods=["POST"])
def create_permiso():
    """
    Create permisos
    """
    try:
        permisos_validate = permisosCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_permisos = validate_permisos(permisos_validate.id_permiso)
    if data_permisos:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_permisos = create_permisos(permisos_validate.dict(exclude_unset=True))
    return {
				"message": "permisos creada exitosamente",
				"status": 1,
				"data": {
                    "id_permiso": int(data_permisos.id_permiso),
                }
				
			}

@api_permisos.route("/", methods=["PUT"])
def update___permisos():
    """
    Create permisos
    """
    try:
        permisos_validate = permisosUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_permisos = validate_permisos(int(permisos_validate.id_permiso))
    if not data_permisos:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    permisos_update = permisos_validate.dict(exclude_unset=True)
    if not permisos_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_permisos = update_permisos(int(permisos_validate.id_permiso, permisos_update))
    return {
       
        "message": "permisos actualizado exitosamente",
        "status": 1,
        "data": data_permisos,
    }



@api_permisos.route("/<int:id_permiso>", methods=["GET"]) 
def get_only_permisos(id_permiso: str):
    """
    Create permisos
    """
    permisos = validate_permisos(id_permiso)
    if not permisos:
        return jsonify({"errors": "No existe un registro con este id","status": -1,}), 400
    
    data_permisos= format_permisos(permisos)
    return {
            "message": "permisos consulta exitosamente",
            "status": 1,
            "data": data_permisos,
        }
