# tests/test_estados.py
import unittest
from models.estado_cuantico import EstadoCuantico

class TestEstadoCuantico(unittest.TestCase):
    def test_medicion(self):
        estado = EstadoCuantico("test", [1, 0])
        self.assertEqual(estado.medir(), {0: 1.0, 1: 0.0})