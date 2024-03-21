import modules.getAllData as Data
from tabulate import tabulate
from datetime import datetime
import os
import modules.delete as delete

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
                    
                    X.Salir
                    """)
            
            pet = input("Ingrese la opcion a la que quiera acceder: ")
            if pet == "1":
                while True:
                    print(f"""
                        ----Consultas----
                        
                        1.C
                        2.Extraer informacion jefe
                        3.Consutltar empleados representante de ventas 
                        
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
                X = input("Ingrese id del pago a eliminar")
                delete.Pago(X)
                break            
            elif pet1.upper() == "X":
                os.system("clear")
                break
            else:
                print("Esta opcion no es valida")
                input("Presione enter para continuar")
                os.system("clear")