
from pydantic import BaseModel
from typing import Optional

class rolesCreate(BaseModel):
		id_rol:	Optional[int] = None
		nombre_rol:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class rolesUpdate(BaseModel):
		id_rol:	Optional[int] = None
		nombre_rol:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
