from cliente import Cliente


class GestorClientes:

    def __init__(self):
        self.clientes = Cliente.cargar_json()

    # VALIDACIONES

    def existe_id(self, idc):
        return any(c.id_cliente == idc for c in self.clientes)

    def existe_email(self, email):
        return any(c.get_email() == email for c in self.clientes)

    # CRUD
    
    #AGREGAR CLIENTE

    def agregar_cliente(self, cliente):

        if self.existe_id(cliente.id_cliente):
            print("Ya existe un cliente con ese ID")
            return

        if self.existe_email(cliente.get_email()):
            print("Ya existe un cliente con ese Email")
            return

        self.clientes.append(cliente)
        print("Cliente agregado correctamente")

        Cliente.log(
            f"ACCION=CREADO | Cliente | ID={cliente.id_cliente} | Nombre={cliente._nombre} | Email={cliente.get_email()}"
        )

    # EDITAR CLIENTE
    def editar_cliente(self, idc, nuevo_nombre=None, nuevo_email=None, nuevo_telefono=None):

        for c in self.clientes:
            if c.id_cliente == idc:

                if nuevo_nombre:
                    c._nombre = nuevo_nombre

                if nuevo_email:
                    if self.existe_email(nuevo_email) and nuevo_email != c.get_email():
                        print("El email ya está registrado en otro cliente")
                        return
                    c.set_email(nuevo_email)

                if nuevo_telefono:
                    c.set_telefono(nuevo_telefono)

                print("Cliente actualizado correctamente")

                Cliente.log(
                    f"ACCION=EDITADO | Cliente | ID={c.id_cliente} | Nombre={c._nombre} | Email={c.get_email()}"
                )
                return

        print("Cliente no encontrado")

        #MOSTRAR CLIENTES

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados")
            return

        for c in self.clientes:
            c.presentarse()

    def buscar_cliente(self, idc):
        for c in self.clientes:
            if c.id_cliente == idc:
                c.presentarse()
                return c

        print("Cliente no encontrado")
        return None
       
       # ELIMINAR CLIENTE

    def eliminar_cliente(self, idc):
        for c in self.clientes:
            if c.id_cliente == idc:
                self.clientes.remove(c)
                print("Usuario eliminado del sistema")

                Cliente.log(
                    f"ACCION=ELIMINADO | Cliente | ID={c.id_cliente} | Nombre={c._nombre}"
                )
                return

        print("Usuario no encontrado")

    def guardar(self):
        Cliente.guardar_json(self.clientes)
