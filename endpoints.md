# Endpoints

1. **Orders**:

   - `GET /api/orders`: Obtener todos los pedidos del usuario autenticado.
   - `GET /api/orders/{order_id}`: Obtener detalles de un pedido específico.
   - `POST /api/orders`: Realizar un nuevo pedido.
   - `PUT /api/orders/{order_id}`: Actualizar el estado de un pedido (solo para propietarios de tiendas o repartidores).
   - `DELETE /api/orders/{order_id}`: Cancelar un pedido (solo para usuarios o propietarios de tiendas).
   - `GET /api/orders/history`: Obtener historial de pedidos del usuario autenticado.
   - `GET /api/orders/{order_id}/rate`: Obtener la calificación y comentario de un pedido (solo para usuarios).
   - `POST /api/orders/{order_id}/rate`: Calificar y dejar un comentario sobre un pedido (solo para usuarios).

2. **Pagos**:

   - `POST /api/payments`: Realizar un pago por un pedido.
   - `GET /api/payments/{payment_id}`: Obtener detalles de un pago específico.

3. **Promociones y Descuentos**:

   - `GET /api/promotions`: Obtener todas las promociones activas.
   - `GET /api/promotions/{promotion_id}`: Obtener detalles de una promoción específica.
   - `POST /api/promotions`: Crear una nueva promoción (solo para administradores).
   - `PUT /api/promotions/{promotion_id}`: Actualizar una promoción (solo para administradores).
   - `DELETE /api/promotions/{promotion_id}`: Eliminar una promoción (solo para administradores).
