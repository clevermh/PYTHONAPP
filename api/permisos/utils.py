from db.db import session
from sqlalchemy import select
from db.models import permisos
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


def get_permisos():
    query = session.query(
		permisos.id_permiso,
		permisos.nombre_permiso,
		permisos.fecha_creacion,
		permisos.estado,

    ).all()
    data_permisos = []
    for i in query:
        data = dict(i)
        data["id_permiso"] = int(data["id_permiso"]) 
        data_permisos.append(data)
    return data_permisos

def update_permisos(id_permisos, data):
    try:
        data_permisos = permisos(**data)
        session.query(permisos).filter(
            permisos.id_permiso== data_permisos.id_permiso
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_permisos= validate_permisos(int(data_permisos.id_permisos))
    return format_permisos(data_permisos)


def create_permisos(data):
    permisos_data = permisos(**data)
    data_permisos = generic_post(permisos_data)
    return data_permisos

def validate_permisos(id_permiso: int):
    permisos_data = (
        session.query(permisos).filter(permisos.id_permiso == id_permiso).first()
    )
    return permisos_data

def format_permisos(permisos):
    permisos = permisos.__dict__
    permisos.pop("_sa_instance_state")
    permisos["id_permiso"] = int(permisos["id_permiso"]) 
    return permisos

