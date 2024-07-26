import json

class Transacciones:
    def __init__(self):
        self.lista_transacciones = list()

    #getters and setters
    def get_transacciones(self):
        archivo = open(file="json/transacciones.json",mode="r",encoding="utf-8")
        self.lista_transacciones = json.load(archivo)
        archivo.close()
        return self.lista_transacciones      
    
    def set_transacciones(self,nueva_lista_transacciones):
        archivo = open(file="json/transacciones.json",mode="w",encoding="utf-8")
        json.dump(nueva_lista_transacciones,archivo,indent=4)
        archivo.close()  

    #CRUD
    # create
    def agregar_transaccion(self,nueva_transaccion):
        lista_de_transacciones = self.get_transacciones()
        if len(lista_de_transacciones)==0:
            id_ultimo = 0
        else:
            ultimo_transaccion = lista_de_transacciones[-1]
            id_ultimo = ultimo_transaccion['id_transaccion']
        nueva_transaccion['id_transaccion'] = id_ultimo + 1
        lista_de_transacciones.append(nueva_transaccion)
        self.set_transacciones(lista_de_transacciones)

    # read
    def mostrar_transacciones(self):
        lista_de_transacciones = self.get_transacciones()
        return lista_de_transacciones

    # update 
    def editar_transaccion(self,id_transaccion,llave,valor):
        lista_de_transacciones = self.get_transacciones()
        for transaccion in lista_de_transacciones:
            if transaccion['id_transaccion'] == id_transaccion:
                transaccion[llave] = valor
        self.set_transacciones(lista_de_transacciones)

    # delete
    def eliminar_transaccion(self,id_transaccion):
        lista_de_transacciones = self.get_transacciones()
        for transaccion in lista_de_transacciones:
            if transaccion['id_transaccion'] == id_transaccion:
                lista_de_transacciones.remove(transaccion)
        self.set_transacciones(lista_de_transacciones)

    #find
    def buscar_transaccion(self,criterio,buscado):
        lista_de_transacciones = self.get_transacciones()
        coincidencias = list()
        for transaccion in lista_de_transacciones:
            if transaccion[criterio] == buscado:
                coincidencias.append(transaccion)
        return coincidencias
    
    
# trasacciones = Transacciones()
# trasacciones.mostrar_transacciones()
# nueva_transaccion = {
#      "id_transaccion": 1,
#       "id_vehiculo": 6,
#       "id_cliente": 7,
#       "tipo_transaccion": "Venta",
#       "fecha": "2024-04-09",
#       "monto": 2100000,
#       "observaciones": "Venta realizada con éxito."
# }
# #trasacciones.agregar_transaccion(nueva_transaccion)
# #trasacciones.eliminar_transaccion(3)
# #trasacciones.editar_transaccion(2,'monto',800000)
# print("TRANSACCION ...")
##print(trasacciones.buscar_transaccion('tipo_transaccion','Compra'))
#trasacciones.mostrar_transacciones()
