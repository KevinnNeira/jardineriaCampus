import storage.empleado as x
def getempleadosboss(a):
    result = []
    for val in x.empleado:
        if(val.get("codigo_jefe") == a):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email"),
                val.get("codigo_jefe")
            ])   
    return result
    
def getboss():
    result = []
    for val in  x.empleado:
        if(val.get("codio_jefe") == None):
            result.append([
                val.get("puesto"),
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email")
            ])
    return result

def getrepresentanteVentasEmp():
    result = []
    for val in x.empleado:
        if(val.get("puesto") != "Representante Ventas"):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("puesto")
            ])
    return result


