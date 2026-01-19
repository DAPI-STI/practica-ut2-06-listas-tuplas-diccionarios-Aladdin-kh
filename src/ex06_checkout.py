"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    diccionario = {}

    for prod, unid in cart:
        if unid < 0: 
            raise ValueError ("Las unidades no pueden ser negativas")
        if prod not in PRICES:
            raise ValueError("Producto no Existe")
        
        if prod in diccionario:
            diccionario[prod] += unid
        else:
            diccionario[prod] = unid
    dcostes = {}
    total = 0.0
    for prod, unid in diccionario.items():
      cost= PRICES [prod] * unid
      dcostes[prod] = round (cost, 2)
      total += cost
      total = round (total, 2)
    return(dcostes, total)
        