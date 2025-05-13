import numpy as np

class OperadorCuantico:
    def __init__(self, nombre: str, matriz: np.ndarray):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)
        
    def aplicar(self, estado: 'estado_cuantico') -> 'estado_cuantico':
        """Aplica el operador y retorna nuevo estado."""
        nuevo_vector = np.dot(self.matriz, estado.vector)
        return estado_cuantico(
            id=f"{estado.id}_{self.nombre}",
            vector=nuevo_vector,
            base=estado.base
        )
HADAMARD = OperadorCuantico("H", [[1/np.sqrt(2), 1/np.sqrt(2)], ...])
PAULI_X = OperadorCuantico("X", [[0, 1], [1, 0]])