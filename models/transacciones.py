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
        criterios_int = ['id_transaccion','id_vehiculo','id_cliente','monto']
        for criterio in criterios_int:
            if llave == criterio:
                valor = int(valor)
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
        criterios_int = ['id_transaccion','id_vehiculo','id_cliente','monto']
        for transaccion in lista_de_transacciones:
            if criterio in criterios_int:
                buscado = int(buscado)
            if transaccion[criterio] == buscado:
                coincidencias.append(transaccion)
        return coincidencias
    
    
