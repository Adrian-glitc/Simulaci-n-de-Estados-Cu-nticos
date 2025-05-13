import math
import cmath # Para trabajar con números complejos

class EstadoCuantico:
    """
    Representa un estado cuántico individual.
    """

    def __init__(self, id_estado: str, vector: list[complex | float], base: str):
        """
        Inicializa un nuevo estado cuántico.

        Args:
            id_estado (str): Identificador único del estado.
            vector (list[complex | float]): Lista de amplitudes del estado.
                                            Pueden ser números complejos o reales.
            base (str): Descripción de la base en la que está expresado el vector
                        (ej. "computacional", "polarizacion").
        
        Raises:
            ValueError: Si el vector de estado está vacío.
            ValueError: Si el vector de estado no está normalizado (opcional, actualmente comentado).
        """
        if not isinstance(id_estado, str) or not id_estado:
            raise ValueError("El identificador del estado (id_estado) no puede estar vacío y debe ser una cadena.")
        if not isinstance(vector, list) or not vector:
            raise ValueError("El vector de estado no puede estar vacío.")
        if not all(isinstance(amp, (complex, float, int)) for amp in vector):
            raise ValueError("Todas las amplitudes en el vector deben ser números (float o complex).")
        if not isinstance(base, str) or not base:
            raise ValueError("La base del estado no puede estar vacía y debe ser una cadena.")

        self.id_estado = id_estado
        # Aseguramos que todos los elementos del vector sean complejos para consistencia
        self.vector = [complex(amp) for amp in vector]
        self.base = base

        # Opcional: Comprobar si el vector está normalizado (suma de |amplitudes|^2 ≈ 1)
        # self.verificar_normalizacion()

    def verificar_normalizacion(self, tolerancia: float = 1e-9) -> None:
        """
        Verifica si el vector de estado está normalizado.
        La suma de los módulos al cuadrado de las amplitudes debe ser 1.

        Args:
            tolerancia (float): Pequeña tolerancia para comparaciones de punto flotante.
        
        Raises:
            ValueError: Si el vector no está normalizado dentro de la tolerancia.
        """
        suma_cuadrados_modulos = sum(abs(amp)**2 for amp in self.vector)
        if not math.isclose(suma_cuadrados_modulos, 1.0, rel_tol=tolerancia, abs_tol=tolerancia):
            raise ValueError(
                f"El vector de estado para '{self.id_estado}' no está normalizado. "
                f"Suma de |amplitudes|^2 = {suma_cuadrados_modulos}, debería ser 1."
            )

    def medir(self) -> list[float]:
        """
        Calcula las probabilidades de obtener cada estado base al medir el estado cuántico.
        Esto se logra calculando el módulo al cuadrado de cada amplitud del vector.
        No simula el colapso del estado, solo calcula las probabilidades teóricas.

        Returns:
            list[float]: Una lista de probabilidades, donde cada elemento corresponde
                         a la probabilidad de colapsar en el estado base respectivo.
                         Por ejemplo, para un qubit en la base computacional {|0>, |1>},
                         el primer elemento es P(|0>) y el segundo es P(|1>).
        """
        probabilidades = [abs(amplitud)**2 for amplitud in self.vector]
        return probabilidades

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de texto del estado cuántico.
        """
        # Formatear el vector para que los números complejos se vean bien
        vector_str_parts = []
        for amp in self.vector:
            if amp.imag == 0:
                vector_str_parts.append(f"{amp.real:.3f}")
            else:
                vector_str_parts.append(f"({amp.real:.3f}{amp.imag:+.3f}j)")
        vector_str = "[" + ", ".join(vector_str_parts) + "]"
        
        return f"{self.id_estado}: vector={vector_str} en base '{self.base}'"

    def __repr__(self) -> str:
        """
        Devuelve una representación "oficial" del objeto, útil para debugging.
        """
        return f"EstadoCuantico(id_estado='{self.id_estado}', vector={self.vector}, base='{self.base}')"

# --- Ejemplo de uso (para pruebas rápidas) ---
if __name__ == "__main__":
    print("Probando la clase EstadoCuantico:")

    # Estado |0>
    try:
        estado_0 = EstadoCuantico("q0", [1, 0], "computacional")
        print(estado_0)
        print(f"  Probabilidades de medición para {estado_0.id_estado}: {estado_0.medir()}")
        # Descomentar para probar la normalización (debería pasar)
        # estado_0.verificar_normalizacion() 
        # print("  Normalización de q0 verificada.")
    except ValueError as e:
        print(f"Error al crear q0: {e}")

    # Estado |+> = (1/sqrt(2))|0> + (1/sqrt(2))|1>
    sqrt2_inv = 1 / math.sqrt(2)
    try:
        estado_plus = EstadoCuantico("q_plus", [sqrt2_inv, sqrt2_inv], "computacional")
        print(estado_plus)
        print(f"  Probabilidades de medición para {estado_plus.id_estado}: {estado_plus.medir()}")
        # estado_plus.verificar_normalizacion()
        # print("  Normalización de q_plus verificada.")
    except ValueError as e:
        print(f"Error al crear q_plus: {e}")

    # Estado con números complejos: (1/sqrt(2))|0> + (i/sqrt(2))|1>
    try:
        estado_complex = EstadoCuantico("q_complex", [sqrt2_inv, complex(0, sqrt2_inv)], "computacional")
        print(estado_complex)
        print(f"  Probabilidades de medición para {estado_complex.id_estado}: {estado_complex.medir()}")
        # estado_complex.verificar_normalizacion()
        # print("  Normalización de q_complex verificada.")
    except ValueError as e:
        print(f"Error al crear q_complex: {e}")

    # Estado no normalizado (si se activa la verificación, debería fallar)
    try:
        print("\nIntentando crear un estado no normalizado (esperando error si la verificación está activa):")
        estado_no_norm = EstadoCuantico("q_no_norm", [1, 1], "computacional")
        # estado_no_norm.verificar_normalizacion() # Esto lanzaría ValueError
        print(estado_no_norm) # Se imprimirá si la verificación no está en __init__
        print(f"  Probabilidades de medición para {estado_no_norm.id_estado}: {estado_no_norm.medir()}")
    except ValueError as e:
        print(f"Error esperado al crear/verificar q_no_norm: {e}")

    # Pruebas de errores en la inicialización
    print("\nProbando errores de inicialización:")
    try:
        EstadoCuantico("", [1,0], "base")
    except ValueError as e:
        print(f"- Error por ID vacío: {e}")
    try:
        EstadoCuantico("id_test", [], "base")
    except ValueError as e:
        print(f"- Error por vector vacío: {e}")
    try:
        EstadoCuantico("id_test", [1, "no_es_numero"], "base")
    except ValueError as e:
        print(f"- Error por tipo incorrecto en vector: {e}")
    try:
        EstadoCuantico("id_test", [1,0], "")
    except ValueError as e:
        print(f"- Error por base vacía: {e}")
