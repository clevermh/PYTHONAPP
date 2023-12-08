

from db.db import session
from sqlalchemy import select
from db.models import subfuncionalidad
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


def get_subfuncionalidad():
    query = session.query(
		subfuncionalidad.id_subfuncionalidad,
		subfuncionalidad.id_funcionalidad,
		subfuncionalidad.nombre_funcionalidad,
		subfuncionalidad.link,
		subfuncionalidad.icono,
		subfuncionalidad.fecha_creacion,
		subfuncionalidad.estado,
        

    ).all()
    data_subfuncionalidad = []
    for i in query:
        data = dict(i)
        data["id_subfuncionalidad"] = int(data["id_subfuncionalidad"]) 
        data_subfuncionalidad.append(data)
    return data_subfuncionalidad

def update_subfuncionalidad(id_subfuncionalidad, data):
    try:
        data_subfuncionalidad = subfuncionalidad(**data)
        session.query(subfuncionalidad).filter(
            subfuncionalidad.id_subfuncionalidad== data_subfuncionalidad.id_subfuncionalidad
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_subfuncionalidad= validate_subfuncionalidad(int(data_subfuncionalidad.id_subfuncionalidad))
    return format_subfuncionalidad(data_subfuncionalidad)


def create_subfuncionalidad(data):
    subfuncionalidad_data = subfuncionalidad(**data)
    data_subfuncionalidad = generic_post(subfuncionalidad_data)
    return data_subfuncionalidad

def validate_subfuncionalidad(id_subfuncionalidad: int):
    data_subfuncionalidad = (
        session.query(subfuncionalidad).filter(subfuncionalidad.id_subfuncionalidad == id_subfuncionalidad).first()
    )
    return data_subfuncionalidad

def format_subfuncionalidad(subfuncionalidad):
    subfuncionalidad = subfuncionalidad.__dict__
    subfuncionalidad.pop("_sa_instance_state")
    subfuncionalidad["id_subfuncionalidad"] = int(subfuncionalidad["id_subfuncionalidad"]) 
    return subfuncionalidad

