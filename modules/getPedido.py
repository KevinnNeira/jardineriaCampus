import modules.getAllData as Data
from datetime import datetime
from tabulate import tabulate
import os
import modules.delete as delete
import modules.post as post
import modules.update as update

def getEstadoPedid():
    result = []
    for val in Data.Pedido():
        if[val.get("estado")] in result:
            result
        else:
            result.append([val.get("estado")])
    return result

def getPedidoTarde():
    result = []
    for val in Data.Pedido():
        if val.get("fecha_entrega") != None:
            fecha1 = val.get("fecha_entrega")
            fecha2 = val.get("fecha_esperada")
            
            inicio = datetime.strptime(fecha1, "%Y-%m-%d")
            fin = datetime.strptime(fecha2, "%Y-%m-%d")
            
            dife = inicio.date() - fin.date()
            dife = dife.days
    
            result.append([
                val.get("codigo_pedido"),
                val.get("codigo_cliente"),
                val.get("fecha_entrega"),
                val.get("fecha_esperada"),
                dife
                ])
        else:
            result
    else:
        result
    return result

def getPedido2DiasTarde():
    result = []
    for val in Data.Pedido():
        if val.get("fecha_entrega") != None:
            fecha1 = val.get("fecha_entrega")
            fecha2 = val.get("fecha_esperada")
                
            inicio = datetime.strptime(fecha1, "%Y-%m-%d")
            fin = datetime.strptime(fecha2, "%Y-%m-%d")
                
            dife = inicio.date() - fin.date()
            dife = dife.days
            if dife <= -2:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_entrega"),
                        val.get("fecha_esperada"),
                        dife
                    ])
            else:
                result
        else:
            result
    return result

def getpedidosDeEnero():
    result = []
    for val in Data.Pedido():
        fecha = val.get("fecha_entrega")
        estado = val.get("estado")
        if fecha != None and estado == "Entregado":
            fecha = val.get("fecha_entrega")
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            mes = fecha.month
            if mes == 1:
                result.append([
                    val.get("codigo_pedido"),
                    val.get("fecha_entrega"),
                    val.get("fecha_esperada"),
                    val.get("comentario")
                ])
    return result

def menu():
        while True:
            print(f"""----Menu Pedido----
                    
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
                        
                        1.Consultar estado del pedido
                        2.Consultar pedidos tarde
                        3.Consultar pedidos 2 dias tarde
                        4.Consultar pedidos de Enero
                        
                        X.Salir
                        """)
                    break
            
                
                while True:
                    pet1 = input("Ingrese opcion: ")
                    
                    if pet1 == "1":
                        print(tabulate(getEstadoPedid(), headers=["Estado"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                       
                        break
                        
                    elif pet1 == "2":
                        print(tabulate(getPedidoTarde(), headers=["Codigo Pedido","Codigo Cliente","Fecha Entrega","Fecha Esperada"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                       
                        break
                    elif pet1 == "3":
                        print(tabulate(getPedido2DiasTarde(), headers=["Codigo Pedido","Codigo Cliente","Fecha Entrega","Fecha Esperada"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                                              
                        break
                    elif pet1 == "4":
                        print(tabulate(getpedidosDeEnero(), headers=["Codigo Pedido","Fecha Entrega","Fecha Esperada","Comentario"], tablefmt="github"))
                        input("Presiona enter para continuar")
                        os.system("clear")                                              
                        break                    
                    elif pet1.upper() == "X":
                        break
                    else:
                        print("Esta opcion no es valida")
                        input("Presione enter para continuar")
                        os.system("clear")
            elif pet == "2":
                X = input("Ingrese id del pedido a eliminar: ")
                print(f"""
                ----Eliminar----
                
                1.Ingrese el id del pedido que desea eliminar
                """)
                delete.Pedido(X)
                break
            elif pet == "3":
                post.Pedido()
                input("Presiona enter para continuar")
                os.system("clear")
                break
            elif pet == "4":
                X = input("Ingrese el pedido que quiera actualizar: ")
                update.Pedido(X)
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