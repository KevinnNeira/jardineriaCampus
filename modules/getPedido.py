import modules.getAllDAta as Data
from datetime import datetime

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