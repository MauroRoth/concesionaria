import os
class HomeView:
    def __init__(self):
        pass
    
    # limpia la consola
    def clearConsole(self):
        command = "clear"
        if os.name in ("nt", "dos"): 
            command = "cls"
        os.system(command)
    
    def menu(self, controller):
        while True:
            self.clearConsole()
            print("\nMENU CONCECIONARIA")
            print(50*"-")
            print("Menu Vehiculos")
            print(50*"-")
            print("\t\t1. Agregar Vehiculo DOING")
            print("\t\t2. Mostrar Vehiculos DONE")
            print("\t\t3. Editar Vehiculo TODO")
            print("\t\t4. Eliminar Vehiculo TODO")
            print("\t\t5. Buscar en Vehiculos (FALTA VALIDACIONES)")
            print(50*"-")
            print("Menu Clientes")
            print(50*"-")
            print("\t\t6. Agregar Cliente TODO")
            print("\t\t7. Mostrar Clientes DONE")
            print("\t\t8. Editar Cliente TODO")
            print("\t\t9. Eliminar Cliente TODO")
            print("\t\t10. Buscar en Clientes (FALTA VALIDACIONES)")
            print(50*"-")
            print("Menu Transacciones")
            print(50*"-")
            print("\t\t11. Registrar Compra TODO")
            print("\t\t12. Registrar Venta TODO")
            print("\t\t13. Imprimir Transacciones DONE")
            print("\t\t14. Editar Transaccion TODO")
            print("\t\t15. Eliminar Transaccion TODO")
            print("\t\t16. Buscar en Trasacciones (FALTA VALIDACIONES)")
            print(50*"-")
            print("Presione 0 para salir...")
            print(50*"-")

            opcion = input('Ingrese la opcion: ')

            self.clearConsole()
            if opcion == '1': controller.agregar_vehiculo()
            elif opcion == '2': controller.mostrar_vehiculos()
            elif opcion == '3': controller.editar_vehiculo()
            elif opcion == '4': controller.eliminar_vehiculo()
            elif opcion == '5': controller.buscar_en_vehiculos()
            elif opcion == '6': controller.agregar_cliente()
            elif opcion == '7': controller.mostrar_clientes()
            elif opcion == '8': controller.editar_cliente()
            elif opcion == '9': controller.eliminar_cliente()
            elif opcion == '10': controller.buscar_en_clientes()
            elif opcion == '11': controller.registrar_compra()
            elif opcion == '12': controller.registrar_venta()
            elif opcion == '13': controller.imprimir_transacciones()
            elif opcion == '14': controller.editar_transaccion()
            elif opcion == '15': controller.eliminar_transaccion()
            elif opcion == '16': controller.buscar_en_transacciones()
            else: break
        
            input('\nPresione una tecla para continuar... ')
    
    def agregar_vehiculo(self):
        id_vehiculo = 1,
        patente = input('Ingrese Patente: ')
        marca = input('Ingrese Marca: ') 
        modelo = input('Ingrese Modelo: ')
        tipo = input('Ingrese Tipo: ')
        anio = input('Ingrese Año: ')
        kilometraje = input('Ingrese Kilometraje: ')
        precio_compra = input('Ingrese Precio de Compra: ')
        precio_venta = input('Ingrese Precio de Venta: ')
        estado = input('Ingrese Estado: ')
        return [id_vehiculo,patente,marca,modelo,tipo,anio,kilometraje,precio_compra,precio_venta,estado]
    
    def mostrar(self,lista,singular,plural):
        print(f"\nLISTA DE {plural.upper()}\n")
        i = 0
        id_elemento = 'id_'+ singular
        for elemento in lista:
            print(f"* {singular.capitalize()} {elemento[id_elemento]}")
            print(50*"-")
            for clave,valor in elemento.items():
                print(f"\t{clave}: {valor}")
            print(50*"-")
        i+=1
        print(f"Total de {plural}: {len(lista)}")
    
    
    def registrar_compra_view(self):
        pass
    
    def buscar(self,lista_de_criterios,singular,plural):
        print(f"\nBUSQUEDA POR CRITERIOS EN {plural.upper()}\n")
        print(f"Criterios Posibles de {singular.capitalize()}:\n")
        for criterio in lista_de_criterios:
            print(f"\t>\t{criterio}")
        print()
        criterio = input('Ingrese Criterio: ')
        buscado = input("Ingrese la palabra a buscar: ")
        return (criterio,buscado)

 