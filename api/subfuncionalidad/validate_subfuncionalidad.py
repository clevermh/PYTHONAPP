
from pydantic import BaseModel
from typing import Optional

class subfuncionalidadCreate(BaseModel):
		id_subfuncionalidad:	Optional[int] = None
		id_funcionalidad:	Optional[int] = None
		nombre_funcionalidad:	Optional[str] = None
		link:	Optional[str] = None
		icono:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class subfuncionalidadUpdate(BaseModel):
		id_subfuncionalidad:	Optional[int] = None
		id_funcionalidad:	Optional[int] = None
		nombre_funcionalidad:	Optional[str] = None
		link:	Optional[str] = None
		icono:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
