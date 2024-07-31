import json

class Vehiculos:
    def __init__(self):
        self.lista_vehiculos = list()

    #getters and setters
    def get_vehiculos(self):
        archivo = open(file="json/vehiculos.json",mode="r",encoding="utf-8")
        self.lista_vehiculos = json.load(archivo)
        archivo.close()
        return self.lista_vehiculos     
    
    def set_vehiculos(self,nueva_lista_vehiculos):
        archivo = open(file="json/vehiculos.json",mode="w",encoding="utf-8")
        json.dump(nueva_lista_vehiculos,archivo,indent=4)
        archivo.close()     
    #CRUD
    # create
    def agregar_vehiculo(self,nuevo_vehiculo):
        lista_de_vehiculos = self.get_vehiculos()
        if len(lista_de_vehiculos)==0:
            id_ultimo = 0
        else:
            ultimo_vehiculo = lista_de_vehiculos[-1]
            id_ultimo = ultimo_vehiculo['id_vehiculo']
        nuevo_vehiculo['id_vehiculo'] = id_ultimo + 1
        lista_de_vehiculos.append(nuevo_vehiculo)
        self.set_vehiculos(lista_de_vehiculos)

    # read
    def mostrar_vehiculos(self):
        lista_de_vehiculos = self.get_vehiculos()
        return lista_de_vehiculos
    
    # update 
    def editar_vehiculo(self,id_vehiculo,llave,valor):
        lista_de_vehiculos = self.get_vehiculos()
        criterios_int = ['id_vehiculo','año','kilometraje','precio_compra','precio_venta']
        for criterio in criterios_int:
            if llave == criterio:
                valor = int(valor)
        for vehiculo in lista_de_vehiculos:
            if vehiculo['id_vehiculo'] == id_vehiculo:
                vehiculo[llave] = valor
        self.set_vehiculos(lista_de_vehiculos)

    # delete
    def eliminar_vehiculo(self,id_vehiculo):
        lista_de_vehiculos = self.get_vehiculos()
        for vehiculo in lista_de_vehiculos:
            if vehiculo['id_vehiculo'] == id_vehiculo:
                lista_de_vehiculos.remove(vehiculo)
        self.set_vehiculos(lista_de_vehiculos)

    #find
    def buscar_vehiculo(self,criterio,buscado):
        lista_de_vehiculos = self.get_vehiculos()
        coincidencias = list()
        criterios_int = ['id_vehiculo','año','kilometraje','precio_compra','precio_venta']
        for vehiculo in lista_de_vehiculos:
            if criterio in criterios_int:
                buscado = int(buscado)
            if vehiculo[criterio] == buscado:
                coincidencias.append(vehiculo)
        return coincidencias

