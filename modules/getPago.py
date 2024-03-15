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