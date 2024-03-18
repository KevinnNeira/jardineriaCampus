#/bin/python3 /home/Endor-155/jardineriaCampus/main.py

from tabulate import tabulate
import modules.getClients as clientes
import modules.getEmpleados as empleados
import modules.getOficinas as oficinas
import modules.getPago as pago
import modules.getPedido as pedido
import modules.getProducto as producto

print("#1") 
print(tabulate(oficinas.getoficinasciu(),headers=["codigo_oficina","Ciudad"],tablefmt="grid"))

print("#2")
print(tabulate(oficinas.getCiudadTelefonoEspaña(),headers=["ciudad","telefono"],tablefmt="grid"))

print("#3")
print(tabulate(empleados.getempleadosboss(7),headers=["Nombre","Apellido 1","Apellido 2","Email","Codigo Jefe"],tablefmt="grid"))

print("#4")
print(tabulate(empleados.getboss(),headers=["Puesto","Nombre","Apellido 1","Apellido 2","Email"],tablefmt="grid"))

print("#5")
print(tabulate(empleados.getrepresentanteVentasEmp(),headers=["Nombre","Apellido 1","Apellido 2","Puesto"],tablefmt="grid"))

print("#6")
print(tabulate(clientes.getClienteEspaña(),headers=["Nombre Clientes Españoles"],tablefmt="grid"))

print("#7")
print(tabulate(pedido.getEstadoPedid(),headers=["Estados"],tablefmt="grid"))

print("#8")
print(tabulate(pago.getpay(),headers=["codigo_cliente"],tablefmt="grid"))

print("#9")
print(tabulate(pedido.getPedidoTarde(),headers=["Codigo Pedido","Codigo Cliente","Fecha Esperada","Fecha Entrega","Dias de Retrazo"],tablefmt="grid"))

print("#10")
print(tabulate(pedido.getPedido2DiasTarde(),headers=["Codigo Pedido","Codigo Cliente","Fecha Esperada","Fecha Entrega","Dias de Retrazo"],tablefmt="grid"))

print("#11")
print(tabulate(pedido.getEstadoPedid(),headers=["Codigo Pedido","Comentario"],tablefmt="grid"))

print("#12")
print(tabulate(pedido.getpedidosDeEnero(),headers=["Codigo Pedido","Fecha Esperada","Fecha entrega","Comentario"],tablefmt="grid"))

print("#13")
print(tabulate(pago.getPayPaypal2008(),headers=["Forma Pago","Fecha Pedido","Total"],tablefmt="grid"))

print("#14")
print(tabulate(pago.getformasPago(),headers=["Forma Pago"],tablefmt="grid"))

print("#15")
print(tabulate(producto.getornamentales(),headers=["Codigo Producto","Gama","Cantidada En Stock"],tablefmt="grid"))

print("#16")
print(tabulate)