# Roadmap

## Orders [OK]

- [ ] `GET /orders/` Obtener todas las ordenes (IsAdministrator)
- [ ] `POST /orders/` Crear una nueva orden (IsClient)
- [ ] `PATCH /orders/{id}` Actualizar una orden (IsClient)
- [ ] `PATCH /orders/{id}/cancel` Cancelar una orden (IsClient)
- [ ] `GET /orders/available` Obtener lista de pedidos disponibles para aceptar. (IsDriver)
- [ ] `PATCH /orders/{id}/details` Obtener detalles de un pedido (ubicaciones de recogida y entrega) (IsDriver).
- [ ] `POST /orders/{id}/accept` Aceptar un pedido específico (IsDriver).
- [ ] `POST /orders/{id}/reject` Rechazar un pedido específico (IsDriver).
- [ ] `PATCH /orders/{id}/pickup` Marcar pedido como recogido (IsDriver).
- [ ] `PATCH /orders/{id}/deliver` Marcar pedido como entregado (IsDriver).
- [ ] `POST /orders/{id}/rate` Proporcionar calificaciones y feedback sobre un pedido (IsClient).
- [ ] `POST /orders/{id}/report` Reportar un problema con un pedido (IsClient).

## Drivers [OK]

- [x] `GET /drivers` Ver todos los drivers disponibles (IsAdministrator).
- [ ] `POST /drivers/register` Registro de un nuevo conductor.
- [ ] `GET /drivers/profile` obtener en detalle los datos del perfil
- [ ] `PATCH /drivers/profile` actualizar datos del perfil driver
- [ ] `GET /drivers/earnings` Ver detalles de las ganancias.
- [ ] `POST /drivers/withdraw` Solicitar retiro de ganancias acumuladas.
- [ ] `GET /drivers/ratings` Ver calificaciones y comentarios recibidos.
- [ ] `GET /drivers/orders` Ver historial de pedidos realizados por el conductor. (as Done)
- [ ] `PATCH /drivers/availability` Activar o desactivar disponibilidad del conductor. (request.user)

## Payments

Pending implementation

## Promotions

- [ ] `GET /promotions/`
- [ ] `POST /promotions/`
- [ ] `GET /promotions/{id}/`
- [ ] `PUT /promotions/{id}/`
- [ ] `DELETE /promotions/{id}/`
- [ ] `GET /restaurants/{restaurant_id}/promotions/`
- [ ] `POST /restaurants/{restaurant_id}/promotions/`
- [ ] `GET /restaurants/{restaurant_id}/promotions/{promotion_id}/`
- [ ] `PUT /restaurants/{restaurant_id}/promotions/{promotion_id}/`
- [ ] `DELETE /restaurants/{restaurant_id}/promotions/{promotion_id}/`

## Deliveries

- [ ] `GET /deliveries/`
- [ ] `POST /deliveries/`
- [ ] `GET /deliveries/{id}/`
- [ ] `PUT /deliveries/{id}/`
- [ ] `DELETE /deliveries/{id}/`
- [ ] `GET /orders/{order_id}/deliveries/`
- [ ] `POST /orders/{order_id}/deliveries/`
- [ ] `GET /orders/{order_id}/deliveries/{delivery_id}/`
- [ ] `PUT /orders/{order_id}/deliveries/{delivery_id}/`
- [ ] `DELETE /orders/{order_id}/deliveries/{delivery_id}/`

## Coupons

- [ ] `GET /coupons/`
- [ ] `POST /coupons/`
- [ ] `GET /coupons/{id}/`
- [ ] `PUT /coupons/{id}/`
- [ ] `DELETE /coupons/{id}/`
- [ ] `GET /coupons/{coupon_id}/orders/`

## Restaurants [OK]

- [ ] `POST /restaurants/register` Registrar un nuevo restaurant (IsClient).
- [ ] `GET /restaurants` Obtener una lista de todos los restaurantes (AllowAny).
- [ ] `GET //restaurants/{id}` Obtener los detalles de un restaurante específico (AllowAny).
- [ ] `PATCH /restaurants/{id}` Actualizar un restaurante específico (IsPartner).
- [ ] `DELETE /restaurants/{id}/` Eliminar un restaurante específico (IsPartner). [LOGICAL]
- [ ] `GET /restaurants/{id}/orders` Obtener todas las ordenes de un restaurant especifico (IsPartner).
- [ ] `GET /restaurants/{id}/categories` Obtener todas las categorías de un restaurante específico (IsPartner).
- [ ] `GET /restaurants/pending-verification` Obtener una lista de restaurantes que están esperando verificación. (IsSupport)
- [ ] `POST /restaurants/{id}/verify` Marcar un restaurante como verificado (IsSupport).
- [ ] `GET /restaurants/{id}/menu` Obtener el menú de un restaurante específico (lista de alimentos) (AllowAny) [STRUCTURED].
- [ ] `GET /restaurants/{id}/historical` Obtener el historial de cambios de un restaurante específico (IsAdministrator).

- [ ] `GET /restaurants/categories` Obtener una lista de todas las categorías asociadas a un restaurant (IsPartner).
- [ ] `POST /restaurants/categories` Crear una nueva categoría (IsPartner).
- [ ] `PATCH /restaurants/categories/{id}` Actualizar una categoría específica (IsPartner).
- [ ] `DELETE /restaurants/categories/{id}` Eliminar una categoría específica (IsPartner).

- [ ] `GET /restaurants/foods` Obtener una lista de todos los alimentos (IsPartner).
- [ ] `POST /restaurants/foods` Crear un nuevo alimento (IsPartner).
- [ ] `PATCH /restaurants/foods/{id}` Actualizar un alimento específico (IsPartner).
- [ ] `DELETE /restaurants/foods/{id}` Eliminar un alimento específico (IsPartner).
- [ ] `PATCH /restaurants/foods/{id}/feature` Obtener todas las ordenes de un restaurant especifico (IsPartner).
- [ ] `GET /restaurants/foods/{id}/historical` Obtener el historial de cambios de un alimento específico (IsAdministrator).

- [ ] `GET /restaurants/{id}/reviews` Obtener una lista de todas las reseñas para un restaurante específico (AllowAny).
- [ ] `POST /restaurants/{id}/reviews` Crear una nueva reseña para un restaurante específico (IsClient).
- [ ] `GET /restaurants/{id}/reviews/{id}` Obtener los detalles de una reseña específica para un restaurante (IsClient).
- [ ] `PATCH /restaurants/{id}/reviews/{id}` Actualizar una reseña específica para un restaurante (IsClient).
- [ ] `DELETE /restaurants/{id}/reviews/{id}` Eliminar una reseña específica para un restaurante (IsClient).

TODO: Agregar logica de /search en el endpoint /restaurants con filtros

## Blogs [OK]

- [ ] `GET /posts` Obtener una lista de todos los posts (AllowAny).
- [ ] `POST /posts` Crear un nuevo post (IsMarketing).
- [ ] `GET /posts/{id}` Obtener los detalles de un post específico por su ID (AllowAny).
- [ ] `PATCH /posts/{id}` Actualizar un post específico por su ID (IsMarketing).
- [ ] `DELETE /posts/{id}` Eliminar un post específico por su ID (IsMarketing).
- [ ] `POST /posts/{id}/report` Reportar un post específico por su ID (IsClient).
- [ ] `GET /posts/tags` Obtener una lista de todas las etiquetas (IsMarketing).
- [ ] `GET /posts/tags` Crear una nueva etiqueta (IsMarketing).
- [ ] `GET /posts/search/` Buscar posts basados en una consulta de búsqueda (AllowAny).

TODO: recents and featured endpoint unificarlos con /posts agregando un filtro

## Jobs [OK]

- [ ] `GET /positions/` Obtener una lista de todas las posiciones de trabajo (AllowAny).
- [ ] `POST /positions` Crear una nueva posición de trabajo (IsRRHH).
- [ ] `GET /positions/{id}` Obtener los detalles de una posición de trabajo específica por su ID (IsRRHH).
- [ ] `PATCH /positions/{id}` Actualizar una posición de trabajo específica por su ID (IsRRHH).
- [ ] `DELETE /positions/{id}` Eliminar una posición de trabajo específica por su ID (IsRRHH).
- [ ] `GET /workers` Obtener una lista de todos los trabajadores (IsRRHH).
- [ ] `POST /workers` Crear un nuevo trabajador (IsRRHH).
- [ ] `GET /workers/{id}` Obtener los detalles de un trabajador específico por su ID (IsRRHH).
- [ ] `PATCH /workers/{id}` Actualizar un trabajador específico por su ID (IsRRHH).
- [ ] `DELETE /workers/{id}` Eliminar un trabajador específico por su ID (IsRRHH).
- [ ] `POST /workers/{id}/terminate` Dar por terminado un contrato de trabajo (IsRRHH).
- [ ] `POST /applicants/{id}/status` Actualizar el estado de una solicitud de trabajo específica (IsRRHH).
- [ ] `GET /contracts/` Obtener una lista de todos los contratos de trabajo (IsRRHH).
- [ ] `GET /contracts/{id}` Obtener los detalles de un contrato específico por su ID (IsRRHH).

TODO: Agregar permiso para Recursos humanos

## Locations

## Users [OK]

- [ ] `GET /users/reviews` Obtener todas las reseñas escritas por un usuario específico.
- [ ] `GET /users/{id}/historical` Obtener el historial de cambios de un usuario específico (IsAdministrator).

TODO: Agregar reviews a restaurants y posts, limitar modelo de Review

## Logica de Negocios

- [ ] El conductor tendrá un total de 50 puntos si no hace las entregas asignadas se ira descontando este porcentaje, si baja hasta 25 puntos que cambie el estado a ALERT, si baja mas de 10 se elimina la cuenta y se desvincula al driver
- [ ] Al actualizar el estado de una entrega, se podría validar que solo se pueda cambiar a estados específicos y que la fecha de entrega no haya pasado.
- [ ] Cuando se crea una compra, se crea un registro en el modelo Order y se establece el estado de pago como pendiente (payment_status=False).
- [ ] Una vez que el usuario realiza el pago, el estado de pago de la compra se actualiza a pagado (payment_status=True). Este paso puede realizarse a través de un sistema de pagos en línea o algún otro método de confirmación de pago.
- [ ] Cuando el pago se confirma, se activa la entrega asociada a la compra. Esto podría implicar la creación de un registro en el modelo Delivery y la asignación de un conductor para la entrega.
