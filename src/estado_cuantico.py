import numpy as np
from typing import List, Dict

class EstadoCuantico:
    def __init__(self, id: str, vector: List[complex], base: str = "computacional"):
        self.id = id
        self.vector = np.array(vector, dtype=complex)
        self.base = base
        self._normalizar()

    def _normalizar(self) -> None:
        """Normaliza el vector de estado."""
        norma = np.linalg.norm(self.vector)
        if norma != 0:
            self.vector /= norma

    def medir(self) -> Dict[int, float]:
        """Calcula probabilidades de medición."""
        return {i: float(np.abs(amp)**2) for i, amp in enumerate(self.vector)}

    def __str__(self):
        return f"{self.id}: {self.vector} en base {self.base}"

    def to_dict(self):
        """Para serialización en JSON."""
        return {
            "id": self.id,
            "vector": [str(amp) for amp in self.vector],
            "base": self.base
        }