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
        for vehiculo in lista_de_vehiculos:
            if vehiculo[criterio] == buscado:
                coincidencias.append(vehiculo)
        return coincidencias


# vehiculo = Vehiculos()
# nuevo_vehiculo = {
#     "id_vehiculo": 1,
#     "patente": "JTC163",
#     "marca": "Toyota",
#     "modelo": "Etios",
#     "tipo": "Sedán",
#     "año": 2018,
#     "kilometraje": 25000,
#     "precio_compra": 7000000,
#     "precio_venta": 9000000,
#     "estado": "Disponible"
#     }
#vehiculo.agregar_vehiculo(nuevo_vehiculo)
#vehiculo.editar_vehiculo(2,'kilometraje', 74950)
# vehiculo.eliminar_vehiculo(3)
# vehiculo.mostrar_vehiculos()
# print(vehiculo.buscar_vehiculo('marca','Toyota'))
