import numpy as np
from estado_cuantico import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre: str, matriz):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)

        
    def aplicar(self, estado: 'EstadoCuantico') -> 'EstadoCuantico':
        """Aplica el operador y retorna nuevo estado."""
        nuevo_vector = np.dot(self.matriz, estado.vector)
        return EstadoCuantico(
            id=f"{estado.id}_{self.nombre}",
            vector=nuevo_vector,
            base=estado.base
        )
HADAMARD = OperadorCuantico("H", [
    [1/np.sqrt(2),  1/np.sqrt(2)],
    [1/np.sqrt(2), -1/np.sqrt(2)]
])

PAULI_X = OperadorCuantico("X", [[0, 1], [1, 0]])