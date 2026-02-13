import re
from cliente import Cliente, ClientePremium, ClienteCorporativo
from gestion_clientes import GestorClientes

gestor = GestorClientes()
cambios = False

while True:

    print("\n======GESTOR INTELIGENTE DE CLIENTES =====")
    print("1. Agregar Cliente")
    print("2. Mostrar Clientes")
    print("3. Buscar Cliente")
    print("4. Eliminar Cliente")
    print("5. Editar Cliente")
    print("6. Calcular descuento")
    print("7. Guardar")
    print("8. Salir")

    op = input("Seleccione: ")

    try:

        if op == "1":

            print("\n1. Cliente Regular\n2. Cliente Premium\n3. Cliente Corporativo")
            tipo = input("Seleccione tipo de cliente: ")

            if tipo not in ["1", "2", "3"]:
                print("Opción inválida. Ingrese un número del 1 al 3")
                continue

            id_texto = input("ID (4 dígitos): ")
            if not (id_texto.isdigit() and len(id_texto) == 4):
                print("El ID debe tener 4 dígitos")
                continue

            idc = int(id_texto)
            if gestor.existe_id(idc):
                print("ID duplicado")
                continue

            nombre = input("Nombre: ")
            email = input("Email: ")

            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                print("Email inválido (ej: nombre@dominio.com)")
                continue

            telefono = input("Teléfono (+569XXXXXXXX): ")

            if tipo == "1":
                c = Cliente(idc, nombre, email, telefono)
            elif tipo == "2":
                c = ClientePremium(idc, nombre, email, telefono)
            elif tipo == "3":
                c = ClienteCorporativo(idc, nombre, email, telefono)

            gestor.agregar_cliente(c)
            cambios = True

        elif op == "2":
            gestor.listar_clientes()

        elif op == "3":
            idc = int(input("ID: "))
            gestor.buscar_cliente(idc)

        elif op == "4":
            idc = int(input("ID: "))
            gestor.eliminar_cliente(idc)
            cambios = True

        # EDITAR CLIENTE
        elif op == "5":

            idc = int(input("ID del cliente a editar: "))
            c = gestor.buscar_cliente(idc)

            if c:
                print("\nDejar vacío si no desea modificar")

                nuevo_nombre = input("Nuevo nombre: ").strip()
                nuevo_email = input("Nuevo email: ").strip()
                nuevo_telefono = input("Nuevo teléfono (+569XXXXXXXX): ").strip()

                if nuevo_nombre == "":
                    nuevo_nombre = None
                if nuevo_email == "":
                    nuevo_email = None
                if nuevo_telefono == "":
                    nuevo_telefono = None

                gestor.editar_cliente(idc, nuevo_nombre, nuevo_email, nuevo_telefono)
                cambios = True

        elif op == "6":
            idc = int(input("ID cliente: "))
            c = gestor.buscar_cliente(idc)

            if c:
                monto_texto = input("Ingrese monto de la compra: ")
                try:
                    monto = float(monto_texto)
                except ValueError:
                    print("Monto inválido. Debe ingresar solo números (ej: 15000)")
                    continue

                total = c.calcular_descuento(monto)
                print(f"Total a pagar: ${int(round(total)):,}".replace(",", "."))

        elif op == "7":
            gestor.guardar()
            cambios = False
            print("Datos guardados correctamente")

        elif op == "8":
            if cambios:
                gestor.guardar()
                print("Saliendo... Cambios guardados automáticamente")
            else:
                print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Ingrese un número del menú (1-8)")

    except ValueError:
        pass
