"""
EX04 (Tuplas)
Trabajar con una lista de tuplas (nombre, nota) y devolver una tupla.
"""

def best_student(records: list[tuple[str, float]]) -> tuple[str, float]:
    """
    Recibe una lista de tuplas (nombre, nota) y devuelve la tupla del alumno con mayor nota.

    - Si records está vacío, lanza ValueError.
    - Si hay empate, devuelve el primero que aparezca con esa nota.

    Ejemplo:
    [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)] -> ("Luis", 9.0)
    """
    if not records:
        raise ValueError("La lista de registros está vacía.")
    elif len(records) == 1:
        return records[0]
    else:
        best = records[0]
        for record in records:
            if record[1] > best[1]:
                best = record
        return best
    raise NotImplementedError("Implementa best_student(records)")
