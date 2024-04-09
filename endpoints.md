# Endpoints

1. **Tiendas**:

   - `GET /api/restaurants`: Obtener todas las tiendas.
   - `GET /api/restaurants/{restaurant_id}`: Obtener detalles de una tienda específica.
   - `POST /api/restaurants`: Crear una nueva tienda (solo para propietarios de tiendas).
   - `PUT /api/restaurants/{restaurant_id}`: Actualizar detalles de una tienda (solo para propietarios de tiendas).
   - `DELETE /api/restaurants/{restaurant_id}`: Eliminar una tienda (solo para propietarios de tiendas).

2. **Productos**:

   - `GET /api/products`: Obtener todos los productos.
   - `GET /api/products/{product_id}`: Obtener detalles de un producto específico.
   - `POST /api/products`: Crear un nuevo producto (solo para propietarios de tiendas).
   - `PUT /api/products/{product_id}`: Actualizar detalles de un producto (solo para propietarios de tiendas).
   - `DELETE /api/products/{product_id}`: Eliminar un producto (solo para propietarios de tiendas).

3. **Pedidos**:

   - `GET /api/orders`: Obtener todos los pedidos del usuario autenticado.
   - `GET /api/orders/{order_id}`: Obtener detalles de un pedido específico.
   - `POST /api/orders`: Realizar un nuevo pedido.
   - `PUT /api/orders/{order_id}`: Actualizar el estado de un pedido (solo para propietarios de tiendas o repartidores).
   - `DELETE /api/orders/{order_id}`: Cancelar un pedido (solo para usuarios o propietarios de tiendas).
   - `GET /api/orders/history`: Obtener historial de pedidos del usuario autenticado.
   - `GET /api/orders/{order_id}/rate`: Obtener la calificación y comentario de un pedido (solo para usuarios).
   - `POST /api/orders/{order_id}/rate`: Calificar y dejar un comentario sobre un pedido (solo para usuarios).

4. **Pagos**:

   - `POST /api/payments`: Realizar un pago por un pedido.
   - `GET /api/payments/{payment_id}`: Obtener detalles de un pago específico.

5. **Categorías y Subcategorías**:

   - `GET /api/categories`: Obtener todas las categorías de productos.
   - `GET /api/categories/{category_id}`: Obtener detalles de una categoría específica.
   - `GET /api/categories/{category_id}/subcategories`: Obtener todas las subcategorías de una categoría.
   - `POST /api/categories`: Crear una nueva categoría (solo para administradores).
   - `PUT /api/categories/{category_id}`: Actualizar una categoría (solo para administradores).
   - `DELETE /api/categories/{category_id}`: Eliminar una categoría (solo para administradores).

6. **Promociones y Descuentos**:

   - `GET /api/promotions`: Obtener todas las promociones activas.
   - `GET /api/promotions/{promotion_id}`: Obtener detalles de una promoción específica.
   - `POST /api/promotions`: Crear una nueva promoción (solo para administradores).
   - `PUT /api/promotions/{promotion_id}`: Actualizar una promoción (solo para administradores).
   - `DELETE /api/promotions/{promotion_id}`: Eliminar una promoción (solo para administradores).

7. **Repartidores**:

   - `GET /api/drivers`: Obtener todos los repartidores.
   - `GET /api/drivers/{driver_id}`: Obtener detalles de un repartidor específico.
   - `POST /api/drivers`: Registrar un nuevo repartidor (solo para administradores).
   - `PUT /api/drivers/{driver_id}`: Actualizar detalles de un repartidor (solo para administradores).
   - `DELETE /api/drivers/{driver_id}`: Eliminar un repartidor (solo para administradores).

8. **Chat en Tiempo Real**:

   - `POST /api/chats`: Crear un nuevo chat con un repartidor o tienda.
   - `GET /api/chats/{chat_id}`: Obtener mensajes de un chat específico.
   - `POST /api/chats/{chat_id}/messages`: Enviar un mensaje en un chat existente
