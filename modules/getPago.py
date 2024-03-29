import modules.getAllData as Data
from tabulate import tabulate
from datetime import datetime
import os
import modules.delete as delete
import modules.post as post
import modules.update as update
def getpay():
    result = []
    for val in Data.Pago():
        fecha = val.get("fecha_pago")
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        año = fecha.year
        if año == 2008:
            if [val.get("codigo_cliente")] not in result:
                result.append([
                    val.get("codigo_cliente")
                ])
    return result

def getPayPaypal2008():
    result = []
    for val in Data.Pago():
        fecha = val.get("fecha_pago")
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        año = fecha.year
        if val.get("forma_pago") == "PayPal" and año == 2008:
            result.append([
                val.get("forma_pago"),
                val.get("fecha_pago"),
                val.get("total")
            ])
    result.sort(key=lambda x: x[2], reverse=True)
    return result

def getformasPago():
    result = []
    for val in Data.Pago():
        formap = [val.get("forma_pago")]
        if formap not in result: 
            result.append([
                val.get("forma_pago")
            ])
    return result

def menu():
        while True:
            print(f"""----Menu Pago----
                    
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
                        
                        1.Consultar datos de pago
                        2.Consultar pagos por Paypal en el año 2008
                        3.Consutltar formas de pago
                        
                        X.Salir
                        """)
                    break
            
                
                while True:
                    pet1 = input("Ingrese opcion: ")
                    
                    if pet1 == "1":
                        print(tabulate(getpay(), headers=["Codigo Cliente"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                       
                        break
                        
                    elif pet1 == "2":
                        print(tabulate(getPayPaypal2008(), headers=["Forma pago","Fecha Pago","Total"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                       
                        break
                    elif pet1 == "3":
                        print(tabulate(getformasPago(), headers=["Formas de pago"], tablefmt="github"))
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
                X = input("Ingrese id del pago a eliminar: ")
                print(f"""
                ----Eliminar----
                
                1.Ingrese el id del pago que desea eliminar
                """)
                delete.Pago(X)
                break           
            elif pet == "3":
                post.Pago()
                input("Presiona enter para continuar")
                os.system("clear")
                break
            elif pet == "4":
                X = input("Ingrese el pago que quiera actualizar: ")
                update.Pago(X)
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