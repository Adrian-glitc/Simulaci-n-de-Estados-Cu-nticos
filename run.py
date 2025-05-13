# run.py
import json
import numpy as np
from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico
from src.repositorio_de_estados import RepositorioDeEstados

# Operadores predefinidos
OPERADORES = {
    "X": OperadorCuantico("X", [[0, 1], [1, 0]]),
    "H": OperadorCuantico("H", [[1/np.sqrt(2), 1/np.sqrt(2)], 
                           [1/np.sqrt(2), -1/np.sqrt(2)]]),
    "Z": OperadorCuantico("Z", [[1, 0], [0, -1]])
}

def mostrar_menu():
    print("\n=== Simulador Cuántico ===")
    print("1. Listar estados")
    print("2. Agregar estado")
    print("3. Aplicar operador")
    print("4. Medir estado")
    print("5. Guardar estados")
    print("6. Cargar estados")
    print("0. Salir")

def main():
    repo = RepositorioDeEstados()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n--- Estados Registrados ---")
            print(repo.listar_estados() or "No hay estados registrados")
            
        elif opcion == "2":
            id_estado = input("ID del nuevo estado: ")
            vector_str = input("Vector (ej: '1 0' o '0.707 0.707'): ")
            base = input("Base (ej: computacional): ")
            
            try:
                vector = [complex(x) for x in vector_str.split()]
                estado = EstadoCuantico(id_estado, vector, base)
                if repo.agregar_estado(estado):
                    print(f"Estado {id_estado} agregado exitosamente!")
                else:
                    print("Error: ID ya existe")
            except ValueError:
                print("Error: Formato de vector inválido")
        
        elif opcion == "3":
            id_estado = input("ID del estado a transformar: ")
            print("Operadores disponibles:", ", ".join(OPERADORES.keys()))
            nombre_op = input("Nombre del operador: ")
            
            if nombre_op in OPERADORES:
                nuevo_id = input("ID del nuevo estado (dejar vacío para sobrescribir): ") or None
                resultado = repo.aplicar_operador(id_estado, OPERADORES[nombre_op], nuevo_id)
                if resultado:
                    print(f"Operador aplicado. Nuevo estado: {resultado.id}")
                else:
                    print("Error: Estado no encontrado")
            else:
                print("Error: Operador desconocido")
        
        elif opcion == "4":
            id_estado = input("ID del estado a medir: ")
            estado = repo.obtener_estado(id_estado)
            if estado:
                probs = estado.medir()
                print("\nProbabilidades de medición:")
                for base, prob in probs.items():
                    print(f"  |{base}⟩: {prob*100:.2f}%")
            else:
                print("Error: Estado no encontrado")
        
        elif opcion == "5":
            archivo = input("Nombre del archivo (ej: estados.json): ") or "estados.json"
            if repo.guardar_json(archivo):
                print(f"Estados guardados en {archivo}")
        
        elif opcion == "6":
            archivo = input("Nombre del archivo (ej: estados.json): ") or "estados.json"
            try:
                if repo.cargar_json(archivo):
                    print(f"Estados cargados desde {archivo}")
            except FileNotFoundError:
                print("Error: Archivo no encontrado")
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()