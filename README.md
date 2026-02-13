Gestor Inteligente de Clientes

 Descripción

Este proyecto es un sistema que permite almacenar, buscar, editar, eliminar y calcular descuentos para tres tipos de clientes: Regular, Premium y Corporativo. Los datos de los clientes se almacenan en un archivo JSON y las acciones realizadas se registran en un archivo de log.

El sistema está diseñado con polimorfismo y utiliza validaciones para asegurar que los datos de los clientes sean correctos.

Menú

- Agregar Cliente: Se pueden agregar nuevos clientes con diferentes tipos (Regular, Premium, Corporativo).
- Buscar Cliente: Los clientes pueden ser buscados por su ID.
- Editar Cliente: Permite editar los datos de un cliente existente.
- Eliminar Cliente: Se puede eliminar un cliente del sistema.
- Calcular Descuento: Se calcula un descuento de compra según el tipo de cliente.
- Guardar y Cargar Datos: Los datos se guardan y se cargan de un archivo JSON. Los cambios se registran en un archivo de logs.

Estructura del Proyecto

Gestor_Inteligente_de_Clientes
- cliente.py            Define las clases Cliente, ClientePremium, ClienteCorporativo.
- gestion_clientes.py   Define la clase GestorClientes con métodos CRUD y validaciones.
- main.py               Archivo principal con el menú interactivo para el usuario.
- logs.txt              Archivo para registrar acciones del sistema.
- clientes.json         Archivo JSON donde se almacenan los datos de los clientes.

 Ejemplo de uso:

1. Agregar Cliente
2. Mostrar Clientes
3. Buscar Cliente
4. Eliminar Cliente
5. Editar Cliente
6. Calcular descuento
7. Guardar
8. Salir

 Ejemplo de registro de cliente:
Cuando se agrega un cliente, el sistema realiza las siguientes validaciones:
- El ID debe ser único.
- El email debe tener un formato válido.
- El teléfono debe ser del tipo `+569XXXXXXXX`.


