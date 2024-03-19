import storage.cliente as cli
import storage.empleado as emp
import storage.pago as pay

def getClienteEspaña():
    result = []
    for val in cli.cliente:
        if (val.get("pais")== "Spain"):
            result.append([
                val.get("nombre_cliente")
            ])
    return result

#def getClientesMadrid():
#    result = []
#    for val in cli.cliente:
#        region = val.get("region")
#       if region == "Madrid":
#       if region == "Madrid":
#           num1 = val.get("codigo_cliente")
#           num2 = val.get("nombre_cliente")
#           num3 = val.get("pais")
#           num4 = val.get("region")
#           empleado = val.get("codigo_empleado_rep_ventas")
#            if empleado == 11 or empleado == 30:
#                 for val in emp.empleado:
#                    result.append([
#                       num1,num2,num3,num4,
#                       val.get("codigo_empleado"),
#                       val.get("nombre"),
#                       val.get("puesto")
#                   ])
#   return result

def getClientesMadrid():
    result = []
    representantes = [e for e in emp.empleado if e.get("codigo_empleado") in [11, 30]]
    for rep in representantes:
        for val in cli.cliente:
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
    for val in cli.cliente:
        cod = val.get("codigo_empleado_rep_ventas")
        cod2 = val.get("codigo_cliente")
        cod3 = val.get("nombre_cliente")
        for val in emp.empleado:
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
    for val in cli.cliente:
        codigoRep = val.get("codigo_empleado_rep_ventas")
        codigoCli = val.get("codigo_cliente")
        num1 = val.get("codigo_cliente")
        num2 = val.get("nombre_cliente")
        for val in pay.pago:
            if codigoCli == val.get("codigo_cliente"):
                for val in emp.empleado:
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
    for val in pay.pago:
        if val.get("codigo_cliente") not in listCodigoClientePago:
            listCodigoClientePago.append(val.get("codigo_cliente"))
    for val in cli.cliente:
        codigoRepresentante = val.get("codigo_empleado_rep_ventas")
        codigoCliente = val.get("codigo_cliente")
        num1 = val.get("codigo_cliente")
        num2 = val.get("nombre_cliente")
        if codigoCliente not in listCodigoClientePago:
            for val in emp.empleado():
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