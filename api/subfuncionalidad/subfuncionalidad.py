
from flask import Blueprint, jsonify, request 

from api.subfuncionalidad.utils import format_subfuncionalidad
from api.subfuncionalidad.utils import update_subfuncionalidad
from api.subfuncionalidad.utils import create_subfuncionalidad
from api.subfuncionalidad.utils import get_subfuncionalidad, validate_subfuncionalidad

from api.subfuncionalidad.validate_subfuncionalidad import subfuncionalidadCreate ,  subfuncionalidadUpdate

api_subfuncionalidad = Blueprint("Api subfuncionalidad", __name__, url_prefix="/api/subfuncionalidad")

@api_subfuncionalidad.route("/", methods=["GET"])
def getAllsubfuncionalidad():
    """
    Get all subfuncionalidad
    """
    subfuncionalidad = get_subfuncionalidad()
    temsubfuncionalidad=subfuncionalidad
    return {
		"message": " subfuncionalidad consulta exitosamente",
        "status": 1,
        "data": subfuncionalidad,
    }

@api_subfuncionalidad.route("/", methods=["POST"])
def createsubfuncionalidad():
    """
    Create subfuncionalidad
    """
    try:
        subfuncionalidad_validate = subfuncionalidadCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_subfuncionalidad = validate_subfuncionalidad(subfuncionalidad_validate.id_subfuncionalidad)
    if data_subfuncionalidad:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_subfuncionalidad = create_subfuncionalidad(subfuncionalidad_validate.dict(exclude_unset=True))
    return {
				"message": "subfuncionalidad creada exitosamente",
				"status": 1,
				"data": {
                    "id_subfuncionalidad": int(data_subfuncionalidad.id_subfuncionalidad),
                }
				
			}

@api_subfuncionalidad.route("/", methods=["PUT"])
def updatesubfuncionalidad():
    """
    Update subfuncionalidad
    """
    try:
        subfuncionalidad_validate= subfuncionalidadUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_subfuncionalidad = validate_subfuncionalidad(int(subfuncionalidad_validate.id_subfuncionalidad))
    if not data_subfuncionalidad:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    subfuncionalidad_update = subfuncionalidad_validate.dict(exclude_unset=True)
    if not subfuncionalidad_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_subfuncionalidad = update_subfuncionalidad(int(subfuncionalidad_validate.id_subfuncionalidad), subfuncionalidad_update)
    return {
       
        "message": "subfuncionalidad actualizado exitosamente",
        "status": 1,
        "data": data_subfuncionalidad,
    }



@api_subfuncionalidad.route("/<int:id_subfuncionalidad>", methods=["GET"]) 
def get_only_subfuncionalidad(id_subfuncionalidad: str):
    """
    Create subfuncionalidad
    """
    data_subfuncionalidad = validate_subfuncionalidad(id_subfuncionalidad)
    if not data_subfuncionalidad:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    
    data_subfuncionalidad= format_subfuncionalidad(data_subfuncionalidad)
    return {
            "message": "subfuncionalidad consulta exitosamente",
            "status": 1,
            "data": data_subfuncionalidad,
        }
