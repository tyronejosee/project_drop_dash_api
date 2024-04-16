# Endpoints

1. **Repartidores**:

   - `GET /api/drivers`: Obtener todos los repartidores.
   - `GET /api/drivers/{driver_id}`: Obtener detalles de un repartidor específico.
   - `POST /api/drivers`: Registrar un nuevo repartidor (solo para administradores).
   - `PUT /api/drivers/{driver_id}`: Actualizar detalles de un repartidor (solo para administradores).
   - `DELETE /api/drivers/{driver_id}`: Eliminar un repartidor (solo para administradores).

2. **foodos**:

   - `GET /api/foods`: Obtener todos los foods.
   - `GET /api/foods/{food_id}`: Obtener detalles de un food específico.
   - `POST /api/foods`: Crear un nuevo food (solo para propietarios de tiendas).
   - `PUT /api/foods/{food_id}`: Actualizar detalles de un food (solo para propietarios de tiendas).
   - `DELETE /api/foods/{food_id}`: Eliminar un food (solo para propietarios de tiendas).

3. **Menus**:

   - GET /api/menu/: Obtener todos los platos del menú.
   - GET /api/menu/{id}/: Obtener detalles de un plato específico en el menú.
   - POST /api/menu/: Agregar un nuevo plato al menú.
   - PUT /api/menu/{id}/: Actualizar detalles de un plato en el menú.
   - DELETE /api/menu/{id}/: Eliminar un plato del menú.

4. **Pedidos**:

   - `GET /api/orders`: Obtener todos los pedidos del usuario autenticado.
   - `GET /api/orders/{order_id}`: Obtener detalles de un pedido específico.
   - `POST /api/orders`: Realizar un nuevo pedido.
   - `PUT /api/orders/{order_id}`: Actualizar el estado de un pedido (solo para propietarios de tiendas o repartidores).
   - `DELETE /api/orders/{order_id}`: Cancelar un pedido (solo para usuarios o propietarios de tiendas).
   - `GET /api/orders/history`: Obtener historial de pedidos del usuario autenticado.
   - `GET /api/orders/{order_id}/rate`: Obtener la calificación y comentario de un pedido (solo para usuarios).
   - `POST /api/orders/{order_id}/rate`: Calificar y dejar un comentario sobre un pedido (solo para usuarios).

5. **Pagos**:

   - `POST /api/payments`: Realizar un pago por un pedido.
   - `GET /api/payments/{payment_id}`: Obtener detalles de un pago específico.

6. **Promociones y Descuentos**:

   - `GET /api/promotions`: Obtener todas las promociones activas.
   - `GET /api/promotions/{promotion_id}`: Obtener detalles de una promoción específica.
   - `POST /api/promotions`: Crear una nueva promoción (solo para administradores).
   - `PUT /api/promotions/{promotion_id}`: Actualizar una promoción (solo para administradores).
   - `DELETE /api/promotions/{promotion_id}`: Eliminar una promoción (solo para administradores).

7. **Chat en Tiempo Real**:

   - `POST /api/chats`: Crear un nuevo chat con un repartidor o tienda.
   - `GET /api/chats/{chat_id}`: Obtener mensajes de un chat específico.
   - `POST /api/chats/{chat_id}/messages`: Enviar un mensaje en un chat existente
