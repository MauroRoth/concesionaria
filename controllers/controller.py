from models.clientes import Clientes
from models.vehiculos import Vehiculos
from models.transacciones import Transacciones

from views.views import HomeView

class Controller:
    def __init__(self):
        # models
        self.clientes = Clientes()
        self.vehiculos = Vehiculos()
        self.transacciones = Transacciones()
        # views
        self.vista = HomeView()
        
    def menuController(self):
        self.vista.menu(self)

    # opcion 1
    def agregar_vehiculo(self):
        atributos_vehiculo = self.vista.agregar_vehiculo()
        nuevo_vehiculo = {
                "id_vehiculo": atributos_vehiculo[0],
                "patente": atributos_vehiculo[1],
                "marca": atributos_vehiculo[2],
                "modelo": atributos_vehiculo[3],
                "tipo": atributos_vehiculo[4],
                "año": atributos_vehiculo[5],
                "kilometraje": atributos_vehiculo[6],
                "precio_compra": atributos_vehiculo[7],
                "precio_venta": atributos_vehiculo[8],
                "estado": atributos_vehiculo[9]
        }
        self.vehiculos.agregar_vehiculo(nuevo_vehiculo)
        self.vista.mostrar_agregado(nuevo_vehiculo,'Vehículo')

    # opcion 2
    def mostrar_vehiculos(self):
        singular = 'vehiculo'
        plural = 'vehiculos'
        lista_de_vehiculos = self.vehiculos.mostrar_vehiculos()
        self.vista.mostrar(lista_de_vehiculos,singular,plural)

    # opcion 3
    def editar_vehiculo(self): 
        lista_de_vehiculos = self.vehiculos.mostrar_vehiculos()
        id_vehiculo, atributo_a_modificar = self.vista.mostrar_editar_eliminar(lista_de_vehiculos,'editar','Vehículo')
        atributo_modificado = self.vista.modificar_atributo(atributo_a_modificar)
        self.vehiculos.editar_vehiculo(id_vehiculo,atributo_a_modificar,atributo_modificado)
        lista_de_vehiculos = self.vehiculos.mostrar_vehiculos()
        self.vista.mostrar_editar_eliminar(lista_de_vehiculos,'mostrar','Vehículo')

    # opcion 4 
    def eliminar_vehiculo(self):
        lista_de_vehiculos = self.vehiculos.mostrar_vehiculos()
        id_vehiculo = self.vista.mostrar_editar_eliminar(lista_de_vehiculos,'eliminar','Vehículos')
        self.vehiculos.eliminar_vehiculo(id_vehiculo)
        lista_de_vehiculos = self.vehiculos.mostrar_vehiculos()
        self.vista.mostrar_editar_eliminar(lista_de_vehiculos,'mostrar','Vehículos')
        
    
    # opcion 5
    def buscar_en_vehiculos(self):
        lista_de_criterios = ["id_vehiculo","patente","marca","modelo","tipo","año","kilometraje","precio_compra","precio_venta","estado"]
        singular = 'vehiculo'
        plural = 'vehiculos'
        criterio, buscado = self.vista.buscar(lista_de_criterios,singular,plural)
        #validadiciones
        coincidencias = self.vehiculos.buscar_vehiculo(criterio,buscado)
        print(f"\n\t-->>{len(coincidencias)} resultado/s encontrado/s")
        self.vista.mostrar(coincidencias,singular,plural)
    
    # opcion 6
    def agregar_cliente(self):
        atributos_cliente = self.vista.agregar_cliente()
        nuevo_cliente = {
                "id_cliente": atributos_cliente[0],
                "nombre": atributos_cliente[1],
                "apellido": atributos_cliente[2],
                "documento": atributos_cliente[3],
                "direccion": atributos_cliente[4],
                "telefono": atributos_cliente[5],
                "correo_electronico": atributos_cliente[6],
        }
        self.clientes.agregar_cliente(nuevo_cliente)
        self.vista.mostrar_agregado(nuevo_cliente,'Cliente')


    # opcion 7
    def mostrar_clientes(self):
        singular = 'cliente'
        plural = 'clientes'
        lista_de_clientes = self.clientes.mostrar_clientes()
        self.vista.mostrar(lista_de_clientes,singular,plural)
    
    # opcion 8
    def editar_cliente(self): 
        lista_de_clientes = self.clientes.mostrar_clientes()
        id_cliente, atributo_a_modificar = self.vista.mostrar_editar_eliminar(lista_de_clientes,'editar','Cliente')
        atributo_modificado = self.vista.modificar_atributo(atributo_a_modificar)
        self.clientes.editar_cliente(id_cliente,atributo_a_modificar,atributo_modificado)
        lista_de_clientes = self.clientes.mostrar_clientes()
        self.vista.mostrar_editar_eliminar(lista_de_clientes,'mostrar','Cliente')

    # opcion 9
    def eliminar_cliente(self):
        lista_de_clientes = self.clientes.mostrar_clientes()
        id_cliente = self.vista.mostrar_editar_eliminar(lista_de_clientes,'eliminar','Clientes')
        self.clientes.eliminar_cliente(id_cliente)
        lista_de_clientes = self.clientes.mostrar_clientes()
        self.vista.mostrar_editar_eliminar(lista_de_clientes,'mostrar','Clientes')
    
    # opcion 10
    def buscar_en_clientes(self):
        lista_de_criterios = ["id_cliente","nombre","apellido","documento","direccion","telefono","correo_electronico"]
        singular = 'cliente'
        plural = 'clientes'
        criterio, buscado = self.vista.buscar(lista_de_criterios,singular,plural)
        if criterio == 'id_cliente':
            buscado = int(buscado)
        coincidencias = self.clientes.buscar_cliente(criterio,buscado)
        print(f"\n\t-->>{len(coincidencias)} resultado/s encontrado/s")
        self.vista.mostrar(coincidencias,singular,plural)

    # opcion 11
    def registrar_transaccion(self):
        atributos_transaccion = self.vista.agregar_transaccion()
        nueva_transaccion = {
                "id_transaccion": atributos_transaccion[0],
                "id_vehiculo": atributos_transaccion[1],
                "id_cliente": atributos_transaccion[2],
                "tipo_transaccion": atributos_transaccion[3],
                "fecha": atributos_transaccion[4],
                "monto": atributos_transaccion[5],
                "observaciones": atributos_transaccion[6],
        }
        self.transacciones.agregar_transaccion(nueva_transaccion)
        self.vista.mostrar_agregado(nueva_transaccion,'Transacción')

    # opcion 12
    def imprimir_transacciones(self):
        singular = 'transaccion'
        plural = 'transacciones'
        lista_de_transacciones = self.transacciones.mostrar_transacciones()
        self.vista.mostrar(lista_de_transacciones,singular,plural)
    
    # opcion 13
    def editar_transaccion(self): 
        lista_de_transacciones = self.transacciones.mostrar_transacciones()
        id_transaccion, atributo_a_modificar = self.vista.mostrar_editar_eliminar(lista_de_transacciones,'editar','Transacción')
        atributo_modificado = self.vista.modificar_atributo(atributo_a_modificar)
        self.transacciones.editar_transaccion(id_transaccion,atributo_a_modificar,atributo_modificado)
        lista_de_transacciones = self.transacciones.mostrar_transacciones()
        self.vista.mostrar_editar_eliminar(lista_de_transacciones,'mostrar','Transacciones')
    
    # opcion 14
    def eliminar_transaccion(self):
        lista_de_transacciones = self.transacciones.mostrar_transacciones()
        id_transaccion = self.vista.mostrar_editar_eliminar(lista_de_transacciones,'eliminar','Transacciones')
        self.transacciones.eliminar_transaccion(id_transaccion)
        lista_de_transacciones = self.transacciones.mostrar_transacciones()
        self.vista.mostrar_editar_eliminar(lista_de_transacciones,'mostrar','Transacciones')
    
    # opcion 15
    def buscar_en_transacciones(self):
        lista_de_criterios = ["id_transaccion","id_vehiculo","id_cliente","tipo_transaccion","fecha","monto","observaciones"]
        singular = 'transaccion'
        plural = 'transacciones'
        criterio, buscado = self.vista.buscar(lista_de_criterios,singular,plural)
        if criterio == 'id_cliente':
            buscado = int(buscado)
        coincidencias = self.transacciones.buscar_transaccion(criterio,buscado)
        print(f"\n\t-->>{len(coincidencias)} resultado/s encontrado/s")
        self.vista.mostrar(coincidencias,singular,plural)
    