import storage.producto as produc


def getornamentales():
    result = []
    for val in produc.productos:
        ornamentales = val.get("gama")
        stock = val.get("cantidad_en_stock")
        if ornamentales == "Ornamentales" and stock > 100:
            result.append ([
                val.get("codigo_producto"),
                val.get("gama"),
                val.get("cantidad_en_stock")
            ])
    return result