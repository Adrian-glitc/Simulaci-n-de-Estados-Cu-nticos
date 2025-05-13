import json
from typing import Dict, Optional
from .estado_cuantico import EstadoCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados: Dict[str, EstadoCuantico] = {}

    def agregar_estado(self, estado: EstadoCuantico) -> bool:
        if estado.id in self.estados:
            return False
        self.estados[estado.id] = estado
        return True

    def listar_estados(self) -> str:
        return "\n".join(str(estado) for estado in self.estados.values())

    def aplicar_operador(self, id_estado: str, operador: 'OperadorCuantico', nuevo_id: Optional[str] = None) -> Optional[EstadoCuantico]:
        estado = self.estados.get(id_estado)
        if not estado:
            return None
        nuevo_estado = operador.aplicar(estado)
        if nuevo_id:
            nuevo_estado.id = nuevo_id
        self.agregar_estado(nuevo_estado)
        return nuevo_estado

    def guardar_json(self, archivo: str) -> bool:
        with open(archivo, 'w') as f:
            json.dump([estado.to_dict() for estado in self.estados.values()], f, indent=4)
        return True

    def cargar_json(self, archivo: str) -> bool:
        with open(archivo, 'r') as f:
            datos = json.load(f)
            for dato in datos:
                vector = [complex(amp.replace(' ', '')) for amp in dato["vector"]]
                self.agregar_estado(EstadoCuantico(dato["id"], vector, dato["base"]))
        return True