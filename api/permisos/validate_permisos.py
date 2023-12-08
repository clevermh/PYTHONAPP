
from pydantic import BaseModel
from typing import Optional

class permisosCreate(BaseModel):
		id_permiso:	Optional[int] = None
		nombre_permiso:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class permisosUpdate(BaseModel):
		id_permiso:	Optional[int] = None
		nombre_permiso:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
