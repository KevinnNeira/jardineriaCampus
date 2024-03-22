import modules.getAllData as Data
from tabulate import tabulate
import os 
import modules.delete as delete
import modules.post as post
import modules.update as update

def getornamentales(x):
    result = []
    for val in Data.Producto():
        ornamentales = val.get("gama")
        stock = val.get("cantidadEnStock")
        if ornamentales == "Ornamentales" and stock > x:
            result.append ([
                val.get("codigo_producto"),
                val.get("gama"),
                val.get("cantidadEnStock")
            ])
    return result

def menu():
        while True:
            print(f"""----Menu Producto----
                    
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
                        ----Consultas----
                        
                        1.Consulta Cantidad de Ornamentales
                    
                        X.Salir
                        """)
                    break
            
                
                while True:
                    pet1 = input("Ingrese opcion: ")
                    
                    if pet1 == "1":
                        x = int(input("Ingrese la cantidad de Ornamentales: "))
                        print(tabulate(getornamentales(x), headers=["Codigo Producto","Gama","Cantidad en stock"], tablefmt="github"))
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
                X = input("Ingrese id del producto a eliminar: ")
                print(f"""
                ----Eliminar----
                
                1.Ingrese el id del producto que desea eliminar
                """)
                delete.Producto(X)
                break
            elif pet == "3":
                post.Producto()
                break
            elif pet == "4":
                X = input("Ingrese el producto a actualizar: ")
                update.Producto(X)
                break
            elif pet.upper() == "X":
                os.system("clear")
                break
            else:
                print("Esta opcion no es valida")
                input("Presione enter para continuar")
                os.system("clear")