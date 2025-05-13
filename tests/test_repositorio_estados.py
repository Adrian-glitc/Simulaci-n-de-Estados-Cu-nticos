# tests/test_repositorio.py
import unittest
from models.repositorio_de_estados import RepositorioDeEstados
from models.estado_cuantico import EstadoCuantico

class TestRepositorio(unittest.TestCase):
    def test_agregar_estado(self):
        repo = RepositorioDeEstados()
        estado = EstadoCuantico("q1", [0, 1])
        self.assertTrue(repo.agregar_estado(estado))
        self.assertFalse(repo.agregar_estado(estado))  # No duplicados