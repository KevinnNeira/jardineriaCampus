import modules.getAllDAta as Data

def getoficinasciu():
    result = []
    for val in Data.Oficina():
        if(val.get("codigo_oficina")!= None):
            result.append ([
            val.get("codigo_oficina"),
            val.get("ciudad")
        ])
    return result

def getCiudadTelefonoEspaña():
    result = []
    for val in Data.Oficina():
        if(val.get("pais")== "España"):
            result.append ([
                val.get("ciudad"),
                val.get("telefono")
            ])
    return result