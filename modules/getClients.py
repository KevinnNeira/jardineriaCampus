import modules.getAllDAta as Data

def getClienteEspaña():
    result = []
    for val in Data.Cliente():
        if (val.get("pais")== "Spain"):
            result.append([
                val.get("nombre_cliente")
            ])
    return result

def getClientesMadrid():
    result = []
    representantes = [e for e in Data.Empleado if e.get("codigo_empleado") in [11, 30]]
    for rep in representantes:
        for val in Data.Cliente():
            if val.get("region") == "Madrid" and val.get("codigo_empleado_rep_ventas") == rep.get("codigo_empleado"):
                result.append([
                    val.get("codigo_cliente"),
                    val.get("nombre_cliente"),
                    val.get("pais"),
                    val.get("region"),
                    rep.get("codigo_empleado"),
                    rep.get("nombre"),
                    rep.get("puesto")
                ])
    return result

def getRepresentanteClientes():
    result = []
    for val in Data.Cliente():
        cod = val.get("codigo_empleado_rep_ventas")
        cod2 = val.get("codigo_cliente")
        cod3 = val.get("nombre_cliente")
        for val in Data.Empleado:
            if cod == val.get("codigo_empleado"):
                result.append([
                cod2,
                cod3,
                val.get("codigo_empleado"),
                val.get("nombre"),
                f"{val.get('apellido1')} {val.get('apellido2')}"
                ])
    return result

def getpagos():
    result =[]
    for val in Data.Cliente():
        codigoRep = val.get("codigo_empleado_rep_ventas")
        codigoCli = val.get("codigo_cliente")
        num1 = val.get("codigo_cliente")
        num2 = val.get("nombre_cliente")
        for val in Data.Pago():
            if codigoCli == val.get("codigo_cliente"):
                for val in Data.Empleado():
                    if codigoRep == val.get("codigo_empleado"):
                        result.append([
                            num1,
                            num2,
                            val.get("codigo_empleado"),
                            val.get("nombre"),
                            f"{val.get('apellido1')} {val.get('apellido2')}"
                        ])
    return result

def getNopagos():
    result =[]
    listCodigoClientePago = []
    for val in Data.Pago():
        if val.get("codigo_cliente") not in listCodigoClientePago:
            listCodigoClientePago.append(val.get("codigo_cliente"))
    for val in Data.Cliente():
        codigoRepresentante = val.get("codigo_empleado_rep_ventas")
        codigoCliente = val.get("codigo_cliente")
        num1 = val.get("codigo_cliente")
        num2 = val.get("nombre_cliente")
        if codigoCliente not in listCodigoClientePago:
            for val in Data.Empleado():
                if codigoRepresentante == val.get("codigo_empleado"):
                    if codigoCliente not in result:
                        result.append([
                            num1,
                            num2,
                            val.get("codigo_empleado"),
                            val.get("nombre"),
                            f"{val.get('apellido1')} {val.get('apellido2')}"
                        ])
    return result