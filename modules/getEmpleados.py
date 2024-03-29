import modules.getAllData as Data
import os
from tabulate import tabulate
import modules.delete as delete
import modules.post as post
import modules.update as update

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
                2.Eliminar
                3.Añadir
                4.Actualizar
                
                X.Salir
                """)
        
        pet = input("Ingrese la opcion a la que quiera acceder: ")
        if pet == "1":
            while True:
                print(f"""
                    ----Consulta----
                    
                    1.Consultar el id del empleado que desea consultar por codigo de jefe
                    2.Extraer informacion jefe por su codigo
                    3.Consultar empleados representante de ventas
                    
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
                elif pet1.upper() == "X":
                    print("Esta opcion no es valida")
                    input("Presione enter para continuar")
                    os.system("clear")
                    break
                else:
                    print("Esta opcion no es valida")
                    input("Presione enter para continuar")
                    os.system("clear")
        elif pet == "2":
            X = input("Ingrese id del empleado a eliminar: ")
            print(f"""
                ----Eliminar----
                
                1.Ingrese el id del empleado que desea eliminar
                """)
            delete.Empleado(X)
            input("Presiona enter para continuar")
            os.system("clear")
            break                    
        elif pet == "3":
            post.Empleado()
            input("Presiona enter para continuar")
            os.system("clear")
            break
        elif pet == "4":
                X = input("Ingrese el empleado que quiera actualizar: ")
                update.Producto(X)
                input("Presiona enter para continuar")
                os.system("clear")
                break
        elif pet.upper() == "X":
                os.system("clear")
                break
        else:
            print("Esta opcion no es valida")
            input("Presione enter para continuar")
            os.system("clear")
            
            
            
            
            
            
        pet12 = input("Ingrese la opcion a la que quiera acceder: ")
        if pet12 == "1":
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
                pet2 = input("Ingrese opcion: ")
                
                if pet2 == "1":
                    a = int(input("Ingrese el codigo del jefe para eliminar el empleado: "))
                    print(tabulate(getempleadosboss(a), headers=["Nombre","Primer Apellido","Segundo Apellido","Email","Codigo Jefe"], tablefmt="github"))
                    input("Presiona enter para continuar")
                    os.system("clear")
                    break
                elif pet2.upper() == "X":
                    input("Presiona enter para continuar")
                    os.system("clear")
                    break
                else:
                    print("Esta opcion no es valida")
                    input("Presione enter para continuar")
                    os.system("clear")
        elif pet2.upper() == "X":
                os.system("clear")
                break
        else:
            print("Esta opcion no es valida")
            input("Presione enter para continuar")
            os.system("clear")