import os 
import modules as modules
import modules.getEmpleados as Empleados
import modules.getPago as Pago
import modules.getOficinas as Oficinas
import modules.getClients as Clientes
import modules.getProducto as Producto
import modules.getPedido as Pedido

def menu1():
    while True:
        print(f"""
                    ----MENU PRINCIPAL----
                    
                    1.Empleados
                    2.Pago
                    3.Oficinas
                    4.Clientes
                    5.Producto
                    6.Pedido
                    
                    X.Salir
            """)
        
        while True:
            solicitud = input("Ingrese la opcion a la que quiera acceder: ")
            
            if solicitud == "1":
                os.system("clear")
                Empleados.menu()
                break
            elif solicitud == "2":
                os.system("clear")
                Pago.menu()
                break
            elif solicitud == "3":
                os.system("clear")
                Oficinas.menu()
                break
            elif solicitud == "4":
                os.system("clear")
                Clientes.menu()
                break
            elif solicitud == "5":
                os.system("clear")
                Producto.menu()
                break
            elif solicitud == "6":
                os.system("clear")
                Pedido.menu()
                break
            elif solicitud.upper() == "X":
                exit()
            else:
                print("Esta opcion no es valida")
                input("Presione enter para continuar")
                
menu1()