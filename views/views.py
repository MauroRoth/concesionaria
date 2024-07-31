import os, re
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
            print("\nMENÚ CONCESIONARIA")
            print(50*"-")
            print("Menú Vehiculos")
            print(50*"-")
            print("\t\t1. Agregar Vehiculo")
            print("\t\t2. Mostrar Vehiculos")
            print("\t\t3. Editar Vehiculo")
            print("\t\t4. Eliminar Vehiculo")
            print("\t\t5. Buscar en Vehiculos")
            print(50*"-")
            print("Menú Clientes")
            print(50*"-")
            print("\t\t6. Agregar Cliente")
            print("\t\t7. Mostrar Clientes")
            print("\t\t8. Editar Cliente")
            print("\t\t9. Eliminar Cliente")
            print("\t\t10. Buscar en Clientes")
            print(50*"-")
            print("Menú Transacciones")
            print(50*"-")
            print("\t\t11. Registrar Transacción")
            print("\t\t12. Imprimir Transacciones")
            print("\t\t13. Editar Transaccion")
            print("\t\t14. Eliminar Transaccion")
            print("\t\t15. Buscar en Trasacciones")
            print(50*'-')
            print("\t\t16. Buscar Palabras en Todo")
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
            elif opcion == '11': controller.registrar_transaccion()
            elif opcion == '12': controller.imprimir_transacciones()
            elif opcion == '13': controller.editar_transaccion()
            elif opcion == '14': controller.eliminar_transaccion()
            elif opcion == '15': controller.buscar_en_transacciones()
            elif opcion == '16': controller.buscar_palabras()
            else: break

            input('\nPresione una tecla para continuar... ')
    
    def agregar_vehiculo(self):
        print("\nAgregar Vehículo")
        print(50*"-")
        id_vehiculo = None,
        patente = input('Ingrese Patente: ')
        marca = input('Ingrese Marca: ') 
        modelo = input('Ingrese Modelo: ')
        tipo = input('Ingrese Tipo: ')
        anio = int(input('Ingrese Año: '))
        kilometraje = int(input('Ingrese Kilometraje: '))
        precio_compra = int(input('Ingrese Precio de Compra: '))
        precio_venta = int(input('Ingrese Precio de Venta: '))
        estado = input('Ingrese Estado: ')
        return [id_vehiculo,patente,marca,modelo,tipo,anio,kilometraje,precio_compra,precio_venta,estado]
    
    def agregar_cliente(self):
        print("\nAgregar Cliente")
        print(50*"-")
        id_cliente = None,
        nombre = input('Ingrese Nombre: ')
        apellido = input('Ingrese Apellido: ') 
        documento = input('Ingrese Documento: ')
        direccion = input('Ingrese Dirección: ')
        telefono = input('Ingrese Teléfono: ')
        correo_electronico = input('Ingrese Correo Electrónico: ')
        return [id_cliente,nombre,apellido,documento,direccion,telefono,correo_electronico]
    
    def agregar_transaccion(self):
        print("\nAgregar Transacción")
        print(50*"-")
        id_transaccion = None,
        id_vehiculo = int(input('Ingrese id del Vehículo: '))
        id_cliente = int(input('Ingrese id del Cliente: '))
        tipo_transaccion = input('Ingrese Tipo de Transacción: ')
        fecha = input('Ingrese Fecha: ') 
        monto = int(input('Ingrese Monto: '))
        observaciones = input('Ingrese Observaciones: ')
        return [id_transaccion,id_vehiculo,id_cliente,tipo_transaccion,fecha,monto,observaciones]

    def mostrar_agregado(self,nuevo_agregado,categoria):
        print(f"\n\n\t{categoria.capitalize()} Agragado")
        print(50*"-")
        for clave, valor in nuevo_agregado.items():
            print(f"\t{clave}: {valor}")

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
    
    def mostrar_editar_eliminar(self,lista,proceso,categoria):
        for elemento in lista:
            claves = list(elemento.keys())[0:6]
            valores = list(elemento.values())[0:6]
            if elemento == lista[0]:
                for clave in claves:
                    print(f"{clave:^12}", end='')
                print('\n')
            for valor in valores:
                print(f"{valor:^12}", end='')
            print()
        if proceso == 'editar':
            id_categoria = int(input(f'Ingrese el id del {categoria} a Editar: '))
            atributo_a_modificar = input('Ingrese el atributo a modificar: ')
            return id_categoria,atributo_a_modificar
        if proceso == 'eliminar':
            id_categoria = int(input(f'Ingrese el id del {categoria} a Eliminar: '))
            return id_categoria

    def modificar_atributo(self, atributo_a_modificar):
        print(f"Modifique {atributo_a_modificar}")
        atributo_modificado = input('Ingrese modificación: ')
        return atributo_modificado
    
    def buscar(self,lista_de_criterios,singular,plural):
        print(f"\nBUSQUEDA POR CRITERIOS EN {plural.upper()}\n")
        print(f"Criterios Posibles de {singular.capitalize()}:\n")
        for criterio in lista_de_criterios:
            print(f"\t>\t{criterio}")
        print()
        criterio = input('Ingrese Criterio: ')
        buscado = input("Ingrese la palabra a buscar: ")
        return (criterio,buscado)
    
    def buscar_palabras(self):
        palabra_buscada = input('Ingrese palabra a buscar: ')
        return palabra_buscada
    
    def mostrar_coincidencias(self,palabra_buscada,vehiculos,clientes,transacciones):
        for vehiculo in vehiculos:
            for elemento in vehiculo.values():
                elemento = str(elemento)
                if re.findall(palabra_buscada,elemento):
                    for clave,valor in vehiculo.items():
                        print(f"\t{clave}: {valor}")
                    print(50*"-")

        for cliente in clientes:
            for elemento in cliente.values():
                elemento = str(elemento)
                if re.findall(palabra_buscada,elemento):
                    for clave,valor in cliente.items():
                        print(f"\t{clave}: {valor}")
                    print(50*"-")

        for transaccion in transacciones:
            for elemento in transaccion.values():
                elemento = str(elemento)
                if re.findall(palabra_buscada,elemento):
                    for clave,valor in transaccion.items():
                        print(f"\t{clave}: {valor}")
                    print(50*"-")

 