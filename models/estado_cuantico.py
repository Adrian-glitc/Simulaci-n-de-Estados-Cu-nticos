import numpy as np
from typing import List, Dict, Any

class EstadoCuantico:
    def __init__(self, id: str, vector: List[complex], base: str = "computacional"):
        self.id = id
        self.vector = np.array(vector, dtype=complex)
        self.base = base
        self._normalizar()

    def _normalizar(self) -> None:
        """Normaliza el vector de estado."""
        norma = np.sqrt(np.sum(np.abs(self.vector)**2))
        if norma != 0:
            self.vector /= norma

    def medir(self) -> Dict[int, float]:
        """Calcula las probabilidades de medición."""
        return {i: float(np.abs(amp)**2) for i, amp in enumerate(self.vector)}

    def __eq__(self, other) -> bool:
        """Compara estados (útil para evitar duplicados)."""
        return np.allclose(self.vector, other.vector) and self.base == other.base

    def to_dict(self) -> Dict[str, Any]:
        """Serialización para guardar en archivo."""
        return {
            "id": self.id,
            "vector": [str(amp) for amp in self.vector],  # Complex to string
            "base": self.base
        }