
from flask import Blueprint, jsonify, request
from api.usuario.utils import format_usuario
from api.usuario.utils import update_usuario
from api.usuario.utils import create_usuario 
from api.usuario.utils import get_usuario, validate_usuario 

from api.usuario.validate_usuario import usuarioCreate ,  usuarioUpdate

api_usuario = Blueprint("Api usuario", __name__, url_prefix="/api/usuario")

@api_usuario.route("/", methods=["GET"])
def getAllusuario():
    """
    Get all usuario
    """
    data_usuario = get_usuario()
    return {
		"message": " usuario consulta exitosamente",
        "status": 1,
        "data": data_usuario,
    }

@api_usuario.route("/", methods=["POST"])
def createusuario():
    """
    Create usuario
    """
    try:
        usuario_validate = usuarioCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_usuario = validate_usuario(usuario_validate.id_usuario)
    if data_usuario:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_usuario = create_usuario(usuario_validate.dict(exclude_unset=True))
    return {
				"message": "usuario creada exitosamente",
				"status": 1,
				"data": {
                    "id_usuario": int(data_usuario.id_usuario),
                }
				
			}

@api_usuario.route("/", methods=["PUT"])
def updateusuario():
    """
    Create usuario
    """
    try:
        usuario_validate = usuarioUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_usuario = validate_usuario(int(usuario_validate.id_usuario))
    if not data_usuario:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    usuario_update = usuario_validate.dict(exclude_unset=True)
    if not usuario_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_usuario = update_usuario(int(usuario_validate.id_usuario), usuario_update)
    return {
       
        "message": "usuario actualizado exitosamente",
        "status": 1,
        "data": data_usuario,
    }



@api_usuario.route("/<int:id_usuario>", methods=["GET"]) 
def get_only_usuario(id_usuario: str):
    """
    Create usuario
    """
    data_usuario = validate_usuario(id_usuario)
    if not data_usuario:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    
    data_usuario= format_usuario(data_usuario)
    return {
            "message": "usuario consulta exitosamente",
            "status": 1,
            "data": data_usuario,
        }
