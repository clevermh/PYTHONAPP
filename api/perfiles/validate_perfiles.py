from pydantic import BaseModel
from typing import Optional


class PerfilesCreate(BaseModel):
    id_perfil:  Optional[int] = None  
    nombre_perfil: Optional[str] = None
    fecha_creacion: Optional[str] = None
    estado: Optional[int] = None


class PerfilesUpdate(BaseModel):
    id_perfil:  Optional[int] = None  
    nombre_perfil: Optional[str] = None
    fecha_creacion: Optional[str] = None
    estado: Optional[int] = None