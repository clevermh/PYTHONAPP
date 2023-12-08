from flask import Blueprint, jsonify, request 
from api.perfiles.utils import create_perfil,format_perfil, get_perfiles, update_perfil, validate_perfil

from api.perfiles.validate_perfiles import PerfilesCreate, PerfilesUpdate
api_perfiles = Blueprint("Api Controller", __name__, url_prefix="/api/perfiles")

@api_perfiles.route("/", methods=["GET"])
def get_perfil():
    """
    Get all perfiles
    """
    perfiles_db = get_perfiles()
    return {
        "message": "Perfil consulta exitosamente",
        "status": 1,
        "data": perfiles_db,
    }

@api_perfiles.route("/", methods=["POST"])
def create_perfiles():
    """
    Create perfiles
    """
    try:
        perfiles_validate = PerfilesCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    perfiles = validate_perfil(perfiles_validate.id_perfil)
    if perfiles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    perfiles_db = create_perfil(perfiles_validate.dict(exclude_unset=True))
    return {
    
        "message": "Perfil creada exitosamente",
        "status": 1,
        "data": {
                    "id_perfil": int(perfiles_db.id_perfil),
                }
    }

@api_perfiles.route("/", methods=["PUT"])
def update_perfiles():
    """
    Create funcionality
    """
    try:
        perfil_validate = PerfilesUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    perfil = validate_perfil(int(perfil_validate.id_perfil))
    if not perfil:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    perfil_update = perfil_validate.dict(exclude_unset=True)
    if not perfil_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    perfiles_db = update_perfil(int(perfil_validate.id_perfil), perfil_update)
    return {
       
        "message": "Perfil actualizado exitosamente",
        "status": 1,
        "data": perfiles_db,
    }

@api_perfiles.route("/<int:id_perfiles>", methods=["GET"])
def get_only_perfiles(id_perfiles: str):
    """
    Create perfiles
    """
    perfil = validate_perfil(id_perfiles)
    if not perfil:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    perfiles_db= format_perfil(perfil)
    return {
            "message": "Perfil consulta exitosamente",
            "status": 1,
            "data": perfiles_db,
        }