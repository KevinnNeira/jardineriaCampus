import modules.getAllDAta as Data
import os
from tabulate import tabulate

def getempleadosboss(a):
    result = []
    for val in Data.Empleado():
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
    for val in  Data.Empleado():
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
    for val in Data.Empleado():
        if(val.get("puesto") != "Representante Ventas"):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("puesto")
            ])
    return result


def menu():
    while True:
        print(f"""----Menu Empleados----
                
                1.Consulta
                
                X.Salir
                """)
        
        pet = input("Ingrese la opcion a la que quiera acceder: ")
        if pet == "1":
            while True:
                print(f"""
                    ----Consultas----
                    
                    1.Consultar empleados según codigo de jefe
                    2.Extraer informacion jefe
                    3.Consutltar empleados representante de ventas 
                    
                    X.Salir
                    """)
                break
        
            
            while True:
                pet1 = input("Ingrese opcion: ")
                
                if pet1 == "1":
                    a = int(input("Ingrese el codigo del jefe para buscar los empleados: "))
                    print(tabulate(getempleadosboss(a), headers=["Nombre","Primer Apellido","Segundo Apellido","Email","Codigo Jefe"], tablefmt="github"))
                    input("Presiona enter para continuar")
                    os.system("clear")
                    break
                    
                elif pet1 == "2":
                    getboss()
                    break
                elif pet1 == "3":
                    getrepresentanteVentasEmp()
                    break
                elif pet1.upper() == "X":
                    break
                else:
                    print("Esta opcion no es valida")
                    input("Presione enter para continuar")
                    os.system("clear")
        else:
            print("Esta opcion no es valida")
            input("Presione enter para continuar")
            os.system("clear")