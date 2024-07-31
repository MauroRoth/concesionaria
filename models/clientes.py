import json

class Clientes:
    def __init__(self):
        self.lista_clientes = list()
    
    #getters and setters
    def get_clientes(self):
        archivo = open(file="json/clientes.json",mode="r",encoding="utf-8")
        self.lista_clientes = json.load(archivo)
        archivo.close()
        return self.lista_clientes      
    
    def set_clientes(self,nueva_lista_clientes):
        archivo = open(file="json/clientes.json",mode="w",encoding="utf-8")
        json.dump(nueva_lista_clientes,archivo,indent=4)
        archivo.close()     
    
    #CRUD
    # create
    def agregar_cliente(self,nuevo_cliente):
        lista_de_clientes = self.get_clientes()
        if len(lista_de_clientes)==0:
            id_ultimo = 0
        else:
            ultimo_cliente = lista_de_clientes[-1]
            id_ultimo = ultimo_cliente['id_cliente']
        nuevo_cliente['id_cliente'] = id_ultimo + 1
        lista_de_clientes.append(nuevo_cliente)
        self.set_clientes(lista_de_clientes)
    
    # read
    def mostrar_clientes(self):
        lista_de_clientes = self.get_clientes()
        return lista_de_clientes
    
    # update 
    def editar_cliente(self,id_cliente,llave,valor):
        lista_de_clientes = self.get_clientes()
        for cliente in lista_de_clientes:
            if cliente['id_cliente'] == id_cliente:
                cliente[llave] = valor
        self.set_clientes(lista_de_clientes)

    # delete
    def eliminar_cliente(self,id_cliente):
        lista_de_clientes = self.get_clientes()
        for cliente in lista_de_clientes:
            if cliente['id_cliente'] == id_cliente:
                lista_de_clientes.remove(cliente)
        self.set_clientes(lista_de_clientes)

    #find
    def buscar_cliente(self,criterio,buscado):
        lista_de_clientes = self.get_clientes()
        coincidencias = list()
        criterios_int = ['id_cliente']
        for cliente in lista_de_clientes:
            if criterio in criterios_int:
                buscado = int(buscado)
            if cliente[criterio] == buscado:
                coincidencias.append(cliente)
        return coincidencias


cliente = Clientes()
nuevo_cliente = {
        "id_cliente": 0,
        "nombre": "Luis",
         "apellido": "Mani",
          "documento": "234556d3232",
          "direccion": "Calle Franqueza",
          "telefono": "123-4337",
          "correo_electronico": "jaoliva@example.com"
      }
# cliente.agregar_cliente(nuevo_cliente)
# cliente.mostrar_clientes()
# #cliente.editar_cliente(2,'correo_electronico','beniijua@example.com')
# cliente.eliminar_cliente(6)
# cliente.mostrar_clientes()
# # print(cliente.buscar_cliente('nombre','Benito'))
