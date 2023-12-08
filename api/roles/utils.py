

from db.db import session
from sqlalchemy import select
from db.models import roles
from flask import Blueprint, jsonify, request 
from sqlalchemy.orm import Session

def generic_post(data):
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
    except Exception as e:
       
        session.rollback()
        raise Exception("Error al crear el registro")
    return data


def get_roles():
    query = session.query(
		roles.id_rol,
		roles.nombre_rol,
		roles.fecha_creacion,
		roles.estado,

    ).all()
    data_roles = []
    for i in query:
        data = dict(i)
        data["id_rol"] = int(data["id_rol"]) 
        data_roles.append(data)
    return data_roles

def update_roles(id_roles, data):
    try:
        data_roles = roles(**data)
        session.query(roles).filter(
            roles.id_rol== data_roles.id_rol
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_roles= validate_roles(int(data_roles.id_rol))
    return format_roles(data_roles)


def create_roles(data):
    roles_data = roles(**data)
    data_roles = generic_post(roles_data)
    return data_roles

def validate_roles(id_roles: int):
    data_roles = (
        session.query(roles).filter(roles.id_rol == id_roles).first()
    )
    return data_roles

def format_roles(roles):
    roles = roles.__dict__
    roles.pop("_sa_instance_state")
    roles["id_rol"] = int(roles["id_rol"]) 
    return roles

