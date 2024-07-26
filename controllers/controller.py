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
        atributos_vehiculos = self.vista.agregar_vehiculo()
        nuevo_vehiculo = {
                "id_vehiculo": atributos_vehiculos[0],
                "patente": atributos_vehiculos[1],
                "marca": atributos_vehiculos[2],
                "modelo": atributos_vehiculos[3],
                "tipo": atributos_vehiculos[4],
                "año": atributos_vehiculos[5],
                "kilometraje": atributos_vehiculos[6],
                "precio_compra": atributos_vehiculos[7],
                "precio_venta": atributos_vehiculos[8],
                "estado": atributos_vehiculos[9]
        }
        self.vehiculos.agregar_vehiculo(nuevo_vehiculo)

    # opcion 2
    def mostrar_vehiculos(self):
        singular = 'vehiculo'
        plural = 'vehiculos'
        lista_de_vehiculos = self.vehiculos.mostrar_vehiculos()
        self.vista.mostrar(lista_de_vehiculos,singular,plural)

    # opcion 3
    def editar_vehiculo(self):
        print("Edito  Vehiculo")
    
    # opcion 4 
    def eliminar_vehiculo(self):
        print("Elimino Vehiculo")
    
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
        print("agrego cliente")

    # opcion 7
    def mostrar_clientes(self):
        singular = 'cliente'
        plural = 'clientes'
        lista_de_clientes = self.clientes.mostrar_clientes()
        self.vista.mostrar(lista_de_clientes,singular,plural)
    
    # opcion 8
    def editar_cliente(self):
        print("edito un cliente")

    # opcion 9
    def eliminar_cliente(self):
        print("elimino un cliente")
    
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
    def registrar_compra(self):
        print("REGISTRO DE UNA COMPRA")
        # id_transaccion = 0,
        # id_vehiculo_buscado = input('ingrese id_vehiculo que busca: ')
        # coincidencia = self.vehiculos.buscar_vehiculo('id_vehiculo',id_vehiculo_buscado)
        # print(coincidencia)
        # id_cliente_buscado = input('ingrese id_cliente que busca: ')
        # id_cliente = self.clientes.buscar_cliente('id_cliente', id_cliente_buscado)
        # tipo_transaccion =  "Compra",
        # fecha = "2024-01-15",
        # monto = 15000,
        # observaciones = "Compra realizada con éxito."
        # nueva_transaccion = {
        #     "id_transaccion": id_transaccion,
        #     "id_vehiculo": id_vehiculo,
        #     "id_cliente": id_cliente,
        #     "tipo_transaccion": tipo_transaccion,
        #     "fecha": fecha,
        #     "monto": monto,
        #     "observaciones": observaciones
        # }
        #self.transacciones.agregar_transaccion(nueva_transaccion)

    # opcion 12 
    def registrar_venta(self):
        print("registro una venta")
    
    # opcion 13
    def imprimir_transacciones(self):
        singular = 'transaccion'
        plural = 'transacciones'
        lista_de_transacciones = self.transacciones.mostrar_transacciones()
        self.vista.mostrar(lista_de_transacciones,singular,plural)
    
    # opcion 14
    def editar_transaccion(self):
        print("edito una transaccion")
    
    # opcion 15
    def eliminar_transaccion(self):
        print("elimino una transaccion")
    
    # opcion 16
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
    