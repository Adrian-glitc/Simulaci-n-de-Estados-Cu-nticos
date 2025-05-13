from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico
from src.repositorio_de_estados import RepositorioDeEstados

def main():
    repo = RepositorioDeEstados()
    
    # Ejemplo de uso
    estado1 = EstadoCuantico("q0", [1, 0], "computacional")
    repo.agregar_estado(estado1)
    
    hadamard = OperadorCuantico("H", [[1/np.sqrt(2), 1/np.sqrt(2)], 
                                     [1/np.sqrt(2), -1/np.sqrt(2)]])
    
    repo.aplicar_operador("q0", hadamard, "q0_superpuesto")
    print(repo.listar_estados())
    
    repo.guardar_json("data/estados.json")

if __name__ == "__main__":
    import numpy as np
    main()