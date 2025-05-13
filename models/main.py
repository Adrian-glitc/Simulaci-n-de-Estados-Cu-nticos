from models import EstadoCuantico, OperadorCuantico, RepositorioDeEstados

def main():
    repo = RepositorioDeEstados()
    
    # Crear y agregar un estado
    estado1 = EstadoCuantico("q1", [1+0j, 0j], "computacional")
    repo.agregar_estado(estado1)
    
    # Aplicar operador Hadamard
    hadamard = OperadorCuantico(
        [[1/np.sqrt(2), 1/np.sqrt(2)],
         [1/np.sqrt(2), -1/np.sqrt(2)]],
        "Hadamard"
    )
    repo.aplicar_operador("q1", hadamard, "q1_superpuesto")
    
    # Medir un estado
    print(repo.estados["q1_superpuesto"].medir())  # Output: {0: 0.5, 1: 0.5}
    
    # Guardar y cargar
    repo.guardar_json("data/estados.json")
    repo.cargar_json("data/estados.json")

if __name__ == "__main__":
    main()