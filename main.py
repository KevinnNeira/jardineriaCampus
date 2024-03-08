from tabulate import tabulate
import modules.getClients as clientes
import modules.getEmpleados as empleados
import modules.getOficinas as oficinas
import modules.getPago as pago
import modules.getPedido as pedido

#1 
print(tabulate(oficinas.getoficinasciu(),headers=["codigo_oficina","Ciudad"],tablefmt="grid"))

#2
print(tabulate(oficinas.getCiudadTelefonoEspaña(),headers=["ciudad","telefono"],tablefmt="grid"))

#3
print(tabulate(empleados.getempleadosboss(7),headers=["Nombre","Apellido2","Apellido2"],tablefmt="grid"))

#4
print(tabulate(empleados.getboss(),headers=["Nombre","Apellido1","Apellido2","Email"],tablefmt="grid"))

#5
print(tabulate(empleados.getrepresentanteVentasEmp(),headers=["Nombre","Apellido1","Apellido2","Puesto"],tablefmt="grid"))

#6
print(tabulate(clientes.getClienteEspaña(),headers=["Nombre"],tablefmt="grid"))

#7
print(tabulate(pedido.getEstadoPedid(),headers=["Estados"],tablefmt="grid"))

#8
print(tabulate(pago.getpay(),headers=["codigo_cliente"],tablefmt="grid"))

#9
print(tabulate(pedido.getPedido3DiasTarde(),headers=["codigo_pedido","codigo_cliente","fecha_eperada","fecha_entrega","Dias de retrazo","Comentario"],tablefmt="grid"))

#10
print()