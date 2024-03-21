import modules.getAllData as Data
from tabulate import tabulate
import os
import modules.delete as delete
import modules.post as post

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
        num2 = val.get("nombre_cliente")
        for val in Data.Pago():
            if codigoCli == val.get("codigo_cliente"):
                for val in Data.Empleado():
                    if codigoRep == val.get("codigo_empleado"):
                        result.append([
                            codigoCli,
                            num2,
                            val.get("codigo_empleado"),
                            val.get("nombre"),
                            f"{val.get('apellido1')} {val.get('apellido2')}"
                        ])
    return result

def getNoPagos():
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

def menu():
        while True:
            print(f"""----Menu Clientes----
                    
                    1.Consulta
                    2.Eliminar
                    3.Añadir
                    
                    X.Salir
                    """)
            
            pet = input("Ingrese la opcion a la que quiera acceder: ")
            if pet == "1":
                while True:
                    print(f"""
                        ----Consultas----
                        
                        1.Obtener clientes de España
                        2.Obtener clientes Madrid
                        3.Obtener representante de clientes
                        4.Consulta los pagos
                        5.Consultar los NO pagos
                        
                        X.Salir
                        """)
                    break
            
                
                while True:
                    pet1 = input("Ingrese opcion: ")
                    
                    if pet1 == "1":
                        print(tabulate(getClienteEspaña(), headers=["Nombre Cliente"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                       
                        break
                        
                    elif pet1 == "2":
                        print(tabulate(getClientesMadrid(), headers=["Codigo cliente","Nombre Cliente","Pais","Region","Codigo Empleado","Nombre","Puesto"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                       
                        break
                    elif pet1 == "3":
                        print(tabulate(getRepresentanteClientes(), headers=["Codigo Cliente","Nombre Cliente","Codigo Empleado","Nombre","Apellidos"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")
                        break  
                    elif pet1 == "4":
                        print(tabulate(getpagos(), headers=["Codigo Cliente","Nombre Cliente","Codigo Empleado","Nombre","Apellidos"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                                              
                        break
                    elif pet1 == "5":
                        print(tabulate(getNoPagos(), headers=["Codigo Cliente","Nombre Cliente","Codigo Empleado","Nombre","Apellidos"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                                              
                        break
                    elif pet1.upper() == "X":
                        os.system("clear")
                        break
                    
                    else:
                        print("Esta opcion no es valida")
                        input("Presione enter para continuar")
                        os.system("clear")
            elif pet == "2":
                X = input("Ingrese id del cliente a eliminar: ")
                delete.Cliente(X)
                input("Presiona enter para continuar")
                os.system("clear")
                break
            elif pet.upper() == "X":
                os.system("clear")
                break
            elif pet == "3":
                X = input("Ingrese cliente a añadir: ")
                post.Cliente(X)
                break
            else:
                print("Esta opcion no es valida")
                input("Presione enter para continuar")
                os.system("clear")

