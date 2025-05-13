class OperadorCuantico:
    def __init__(self, matriz: np.ndarray, nombre: str = ""):
        self.matriz = np.array(matriz, dtype=complex)
        self.nombre = nombre

    def aplicar(self, estado: EstadoCuantico) -> EstadoCuantico:
        """Aplica el operador y retorna un NUEVO estado (inmutable)."""
        nuevo_vector = np.dot(self.matriz, estado.vector)
        return EstadoCuantico(
            id=f"{estado.id}_transformado",
            vector=nuevo_vector,
            base=estado.base
        )

    def es_unitario(self) -> bool:
        """Valida si la matriz es unitaria."""
        return np.allclose(
            np.eye(len(self.matriz)),
            np.dot(self.matriz, self.matriz.conj().T)
        )