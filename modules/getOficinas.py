import storage.oficina as ofi

def getoficinasciu():
    result = []
    for val in ofi.oficina:
        if(val.get("codigo_oficina")!= None):
            result.append ([
            val.get("codigo_oficina"),
            val.get("ciudad")
        ])
    return result

def getCiudadTelefonoEspaña():
    result = []
    for val in ofi.oficina:
        if(val.get("pais")== "España"):
            result.append ([
                val.get("ciudad"),
                val.get("telefono")
            ])
    return result