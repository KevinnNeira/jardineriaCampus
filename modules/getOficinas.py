import modules.getAllData as Data
from tabulate import tabulate
import os
import modules.delete as delete
import modules.post as post
import modules.update as update

def getoficinasciu():
    result = []
    for val in Data.Oficina():
        if(val.get("codigo_oficina")!= None):
            result.append ([
            val.get("codigo_oficina"),
            val.get("ciudad")
        ])
    return result

def getPaisTelefonoCiudad(c):
    result = []
    for val in Data.Oficina():
        if(val.get("pais")== c):
            result.append ([
                val.get("codigo_oficina"),
                val.get("pais"),
                val.get("telefono")
            ])
    return result

def menu():
    while True:
        print(f"""----Menu Oficina----
                
                1.Consultar
                2.Eliminar
                3.Añadir
                4.Actualizar
                
                X.Salir
                """)
        
        pet = input("Ingrese la opcion a la que quiera acceder: ")
        if pet == "1":
            while True:
                print(f"""
                    ----Consultas----
                    
                    1.Consultar oficinas con su ciudad
                    2.Consultar oficinas de españa con su telefono
                    
                    X.Salir
                    """)
                break
        
            
            while True:
                pet1 = input("Ingrese opcion: ")
                
                if pet1 == "1":
                    print(tabulate(getoficinasciu(), headers=["Codigo Oficina","Ciudad"], tablefmt="github"))
                    input("Presiona enter para continuar")
                    os.system("clear")
                    break
                    
                elif pet1 == "2":
                    c = input("Ingrese pais a filtrar: ")
                    print(tabulate(getPaisTelefonoCiudad(c), headers=["Codigo Oficina", "Pais","Telefono"], tablefmt="github"))
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
            X = input("Ingrese id de la oficina a eliminar: ")
            print(f"""
                ----Eliminar----
                
                1.Ingrese el id de la oficina que desea eliminar
                """)
            delete.Oficina(X)
            input("Presiona enter para continuar")
            os.system("clear")
            break                   
        elif pet == "3":
            post.Oficina()
            break
        elif pet == "4":
                X = input("Ingrese la oficina que quiera actualizar: ")
                update.Oficina(X)
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