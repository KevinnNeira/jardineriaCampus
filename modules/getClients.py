import modules.getClients as cli

def search():
    clientName: []
    for i, val in enumerate(cli.cliente):
        clientName.append({
            "nombre_cliente": val.get("nombre_cliente"),
            "codigo_cliente": val.get("codigo_cliente")
        })
    return clientName