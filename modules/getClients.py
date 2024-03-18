import storage.cliente as cli
import storage.empleado as emp

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
        codd = val.get("codigo_cliente")
        coddd = val.get("nombre_cliente")
        for val in emp.empleado():
            if cod == "codigo_empleado"