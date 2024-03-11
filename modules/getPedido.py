import storage.pedido as pedi
from datetime import datetime

def getEstadoPedid():
    result = []
    for val in pedi.pedido:
        if[val.get("estado")] in result:
            result
        else:
            result.append([val.get("estado")])
    return result

def getPedidoTarde():
    result = []
    for val in pedi.pedido:
        if val.get("fecha_entrega") != None:
            fecha1 = val.get("fecha_entrega")
            fecha2 = val.get("fecha_esperada")
            
            inicio = datetime.strptime(fecha1, "%Y-%m-%d")
            fin = datetime.strptime(fecha2, "%Y-%m-%d")
            
            dife = inicio.date() - fin.date()
            dife = dife.days
            
            if dife < 0 and val.get("comentario") != None:
                result.append([
                    val.get("codigo_pedido"),
                    val.get("codigo_cliente"),
                    val.get("fecha_entrega"),
                    val.get("fecha_esperada"),
                    dife,
                    val.get("comentario")
                ])
                
            else:
                result.append([
                    val.get("codigo_pedido"),
                    val.get("codigo_cliente"),
                    val.get("fecha_entrega"),
                    val.get("fecha_esperada"),
                    dife,
                    val.get("No hay ningun comentario")
                ])
        else:
            result
    else:
        result
    return result

def getPedido3DiasTarde():
    result = []
    for val in pedi.pedido:
        if val.get("fecha_entrega") != None:
            fecha1 = val.get("fecha_entrega")
            fecha2 = val.get("fecha_esperada")
                
            inicio = datetime.strptime(fecha1, "%Y-%m-%d")
            fin = datetime.strptime(fecha2, "%Y-%m-%d")
                
            dife = inicio.date() - fin.date()
            dife = dife.days
            if dife < -3:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_entrega"),
                        val.get("fecha_esperada"),
                        dife,
                        val.get("comentario")
                    ])
                    
                else:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_entrega"),
                        val.get("fecha_esperada"),
                        dife,
                        val.get("No hay ningun comentario")
                        ])
            else:
                result
        else:
            result
    return result
