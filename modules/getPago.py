import storage.pago as pay
from datetime import datetime

def getpay():
    result = []
    for val in pay.pago:
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
    for val in pay.pago:
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
    for val in pay.pago:
        formap = [val.get("forma_pago")]
        if formap not in result: 
            result.append([
                val.get("forma_pago")
            ])
    return result