"""
EX02 (Listas)
Eliminar duplicados manteniendo el orden de aparición.
"""

def unique_preserve_order(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista sin duplicados, manteniendo el orden.

    Ejemplo:
    - [3, 1, 3, 2, 1] -> [3, 1, 2]

    Requisito:
    - No modifiques la lista original.
    """
    lista1 = set()
    resultado = []
    for i in values:
        if i not in lista1:
            lista1.add(i)
            resultado.append(i)
    return resultado
    raise NotImplementedError("Implementa unique_preserve_order(values)")
