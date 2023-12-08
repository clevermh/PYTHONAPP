
from pydantic import BaseModel
from typing import Optional

class usuarioCreate(BaseModel):
		id_usuario:	Optional[int] = None
		nombre:	Optional[str] = None
		usuario:	Optional[str] = None
		contraseña:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class usuarioUpdate(BaseModel):
		id_usuario:	Optional[int] = None
		nombre:	Optional[str] = None
		usuario:	Optional[str] = None
		contrasena:	Optional[str] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
