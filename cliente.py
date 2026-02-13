import json
import re
from datetime import datetime


class Cliente:
    archivo_json = "clientes.json"
    archivo_logs = "logs.txt"

    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self._nombre = nombre
        self.__email = None
        self.__telefono = None
        self.set_email(email)
        self.set_telefono(telefono)

    # VALIDACIONES

    def set_email(self, email):
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            self.__email = email
        else:
            print("Email inválido")
            self.__email = "email_invalido"

    def get_email(self):
        return self.__email

    def set_telefono(self, tel):
        if re.match(r"^\+569\d{8}$", tel):
            self.__telefono = tel
        else:
            print("Teléfono inválido")
            self.__telefono = "telefono_invalido"

    def get_telefono(self):
        return self.__telefono

    # POLIMORFISMO

    def calcular_descuento(self, monto):
        print("Cliente Regular no tiene descuento")
        return monto

    def presentarse(self):
        print(f"[Cliente Regular] ID:{self.id_cliente} | {self._nombre} | {self.get_email()} | {self.get_telefono()}")

    # JSON

    @classmethod
    def guardar_json(cls, lista):
        datos = []

        for c in lista:
            datos.append({
                "id": c.id_cliente,
                "nombre": c._nombre,
                "email": c.get_email(),
                "telefono": c.get_telefono(),
                "tipo": c.__class__.__name__
            })

        with open(cls.archivo_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        cls.log("ACCION=GUARDADO | Archivo JSON actualizado correctamente")

    @classmethod
    def cargar_json(cls):
        lista = []

        try:
            with open(cls.archivo_json, "r", encoding="utf-8") as f:
                datos = json.load(f)

            for d in datos:
                if d["tipo"] == "ClientePremium":
                    c = ClientePremium(d["id"], d["nombre"], d["email"], d["telefono"])
                elif d["tipo"] == "ClienteCorporativo":
                    c = ClienteCorporativo(d["id"], d["nombre"], d["email"], d["telefono"])
                else:
                    c = Cliente(d["id"], d["nombre"], d["email"], d["telefono"])

                lista.append(c)

        except FileNotFoundError:
            pass

        return lista

    @classmethod
    def log(cls, mensaje):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(cls.archivo_logs, "a", encoding="utf-8") as f:
            f.write(f"[{fecha}] {mensaje}\n")


class ClientePremium(Cliente):

    def calcular_descuento(self, monto):
        descuento = monto * 0.10
        total = monto - descuento
        print("Cliente Premium → 10% de descuento aplicado")
        return total

    def presentarse(self):
        print(f"[Cliente Premium] ID:{self.id_cliente} | {self._nombre} | {self.get_email()} | {self.get_telefono()}")


class ClienteCorporativo(Cliente):

    def calcular_descuento(self, monto):
        descuento = monto * 0.15
        total = monto - descuento
        print("Cliente Corporativo → 15% de descuento aplicado")
        return total

    def presentarse(self):
        print(f"[Cliente Corporativo] ID:{self.id_cliente} | {self._nombre} | {self.get_email()} | {self.get_telefono()}")
