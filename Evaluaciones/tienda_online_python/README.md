# README - Proyecto Tienda Online

Este proyecto implementa una clase `TiendaOnline` en Python, que simula una tienda en línea con funciones como agregar productos al inventario, ver el inventario, buscar productos, actualizar el stock, realizar compras, procesar pagos, y más.

## Librerías Utilizadas

- **re**: Módulo estándar de Python para realizar operaciones con expresiones regulares. [Documentación](https://docs.python.org/3/library/re.html)

## Estructura del Proyecto

- **tienda_online.py**: Contiene la implementación de la clase `TiendaOnline` con sus métodos.

## Uso de la Clase `TiendaOnline`

1. **Instanciar la Tienda Online:**
    ```python
    tienda = TiendaOnline("Mi Tienda")
    ```

2. **Agregar Producto al Inventario:**
    Agrega productos al inventario o actualiza su cantidad y precio si ya existen.
    ```python
    tienda.agregar_producto("Camisa", 20, 50)
    tienda.agregar_producto("Pantalón", 30, 30)
    ```
  

3. **Ver el Inventario:**
    Muestra el inventario de productos con sus detalles (nombre, precio, cantidad).
    ```python
    tienda.ver_inventario()
    ```
    

4. **Buscar un Producto:**
    Busca un producto en el inventario por nombre y muestra sus detalles si se encuentra.
    ```python
    tienda.buscar_producto("Camisa")
    ```
    

5. **Actualizar Stock:**
    Actualiza el stock de un producto en el inventario.
    ```python
    tienda.actualizar_stock("Camisa", -10)
    ```

6. **Eliminar Producto del Inventario:**
    Elimina un producto del inventario por nombre.
    ```python
    tienda.eliminar_producto("Pantalón")
    ```

7. **Calcular Valor del Inventario:**
    Calcula y muestra el valor total del inventario.
    ```python
    tienda.calcular_valor_inventario()
    ```

8. **Buscar Productos por Patrón (Regex):**
    Busca productos en el inventario que coincidan con un patrón de búsqueda en formato regex en el nombre y muestra los resultados.
    ```python
    tienda.buscar_producto_regex("Ca.*")
    ```

9. **Realizar Compra:**
    Permite a un cliente realizar una compra seleccionando productos del inventario.
    ```python
    tienda.realizar_compra()
    ```
    
10. **Procesar Pago:**
    Procesa el pago de una compra, calcula el cambio y muestra un mensaje de confirmación.
    ```python
    tienda.procesar_pago()
    ```

11. **Agregar Cliente:**
    Agrega un nuevo cliente al registro de clientes.
    ```python
    tienda.agregar_cliente("Cliente1", "cliente1@email.com")
    ```

12. **Ver Clientes:**
    Muestra la lista de clientes registrados con sus nombres y correos electrónicos.
    ```python
    tienda.ver_clientes()
    ```

13. **Registrar Compra para un Cliente:**
    Registra una compra para un cliente, actualiza las ventas totales y agrega la compra al historial del cliente.
    ```python
    tienda.registrar_compra("Cliente1", {"Camisa": {"precio": 20, "cantidad": 3}})
    ```


14. **Ver Historial de Compras de un Cliente:**
    Muestra el historial de compras de un cliente, incluyendo detalles de productos y totales.
    ```python
    tienda.ver_compras_cliente("Cliente1")
    ```


15. **Calcular Ventas Totales de la Tienda:**
    Muestra las ventas totales de la tienda.
    ```python
    tienda.calcular_ventas_totales()
    ```

## Métodos incluidos en la clase `TiendaOnline`

- **Método `agregar_producto`:** Este método permite agregar productos al inventario o actualizar su cantidad y precio si ya existen. 

- **Método `ver_inventario`:** Muestra el inventario de productos con sus detalles (nombre, precio, cantidad).

- **Método `buscar_producto`:** Busca un producto en el inventario por nombre y muestra sus detalles si se encuentra.

- **Método `actualizar_stock`:** Actualiza el stock de un producto en el inventario.

- **Método `eliminar_producto`:** Elimina un producto del inventario por nombre.

- **Método `calcular_valor_inventario`:** Calcula y muestra el valor total del inventario.

- **Método `buscar_producto_regex`:** Busca productos en el inventario que coincidan con un patrón de búsqueda en formato regex en el nombre y muestra los resultados.

- **Método `realizar_compra`:** Permite a un cliente realizar una compra seleccionando productos del inventario.

- **Método `procesar_pago`:** Procesa el pago de una compra, calcula el cambio y muestra un mensaje de confirmación.

- **Método `agregar_cliente`:** Agrega un nuevo cliente al registro de clientes.

- **Método `ver_clientes`:** Muestra la lista de clientes registrados con sus nombres y correos electrónicos.

- **Método `registrar_compra`:** Registra una compra para un cliente, actualiza las ventas totales y agrega la compra al historial del cliente.

- **Método `ver_compras_cliente`:** Muestra el historial de compras de un cliente, incluyendo detalles de productos y totales.

- **Método `calcular_ventas_totales`:** Muestra las ventas totales de la tienda.

Este proyecto proporciona una estructura base para una tienda en línea con capacidades de gestión de inventario, clientes, compras, y más. Se pueden realizar pruebas adicionales y personalizaciones según las necesidades específicas del usuario.


## Autoría:
- Este proyecto está realizado por [Karvala](https://github.com/KarvalaCode)