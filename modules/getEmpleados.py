import storage.empleado as x
def getempleadosboss(a):
    result = []
    for val in x.empleado:
        if(val.get("codigo_jefe") == a):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2")
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

def respresentanteVentasEmp():
    result = []
    for val in x.empleado:
        if(val.get("puesto") != "Representante de ventas"):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("puesto")
            ])
            return result