# Roadmap

## Home

- [ ] `GET /home/kwords` Obtener todas las palabras más buscadas (AllowAny). [10]
- [ ] `GET /home/restaurants` Obtener todas los restaurants más popolares (AllowAny). [10]

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

## Promotions [OK]

- [x] `GET /promotions/` Obtener una lista de todas las promociones disponibles (IsMarketing).
- [x] `POST /promotions/` Crear una nueva promoción (IsMarketing).
- [x] `GET /promotions/{id}/` Obtener los detalles de una promoción específica (IsMarketing).
- [x] `PUT /promotions/{id}/` Actualizar todos los detalles de una promoción específica (IsMarketing).
- [x] `PATCH /promotions/{id}/` Actualizar parcialmente una promoción específica (IsMarketing).
- [x] `DELETE /promotions/{id}/` Eliminar una promoción específica (IsMarketing).

- [x] `GET /fixed-coupons/`
- [x] `POST /fixed-coupons/`
- [x] `GET /fixed-coupons/{id}/`
- [x] `PUT /fixed-coupons/{id}/`
- [x] `PATCH /fixed-coupons/{id}/`
- [x] `DELETE /fixed-coupons/{id}/`

- [x] `GET /percentage-coupons/`
- [x] `POST /percentage-coupons/`
- [x] `GET /percentage-coupons/{id}/`
- [x] `PUT /percentage-coupons/{id}/`
- [x] `PATCH /percentage-coupons/{id}/`
- [x] `DELETE /percentage-coupons/{id}/`

## Deliveries

Pending implementation

## Restaurants [OK]

- [x] `GET /restaurants` Obtener una lista de todos los restaurantes (AllowAny).
- [x] `POST /restaurants/` Registrar un nuevo restaurant (IsClient).
- [x] `GET //restaurants/{id}` Obtener los detalles de un restaurante específico (AllowAny).
- [x] `PATCH /restaurants/{id}` Actualizar un restaurante específico (IsPartner).
- [x] `DELETE /restaurants/{id}/` Eliminar un restaurante específico (IsPartner). [LOGICAL]
- [x] `GET /restaurants/{id}/orders` Obtener todas las ordenes de un restaurant especifico (IsPartner).

- [x] `GET /restaurants/{id}/categories` Obtener todas las categorías de un restaurante específico (AllowAny).
- [ ] `GET /restaurants/pending-verification` Obtener una lista de restaurantes que están esperando verificación. (IsSupport)
- [ ] `POST /restaurants/{id}/verify` Marcar un restaurante como verificado (IsSupport).
- [ ] `GET /restaurants/{id}/menu` Obtener el menú de un restaurante específico (lista de alimentos) (AllowAny) [STRUCTURED].
- [ ] `GET /restaurants/{id}/historical` Obtener el historial de cambios de un restaurante específico (IsAdministrator).

- [ ] `GET /categories` Obtener una lista de todas las categorías asociadas a un restaurant (IsPartner).
- [ ] `POST /categories` Crear una nueva categoría (IsPartner).
- [ ] `PATCH /categories/{id}` Actualizar una categoría específica (IsPartner).
- [ ] `DELETE /categories/{id}` Eliminar una categoría específica (IsPartner).

- [ ] `GET /foods` Obtener una lista de todos los alimentos (IsPartner).
- [ ] `POST /foods` Crear un nuevo alimento (IsPartner).
- [ ] `PATCH /foods/{id}` Actualizar un alimento específico (IsPartner).
- [ ] `DELETE /foods/{id}` Eliminar un alimento específico (IsPartner).
- [ ] `PATCH /foods/{id}/feature` Obtener todas las comidas destacadas de un restaurant especifico (IsPartner).
- [ ] `GET /foods/{id}/historical` Obtener el historial de cambios de un alimento específico (IsAdministrator).

- [ ] `GET /restaurants/{id}/reviews` Obtener una lista de todas las reseñas para un restaurante específico (AllowAny).
- [ ] `POST /restaurants/{id}/reviews` Crear una nueva reseña para un restaurante específico (IsClient).
- [ ] `GET /restaurants/{id}/reviews/{id}` Obtener los detalles de una reseña específica para un restaurante (IsClient).
- [ ] `PATCH /restaurants/{id}/reviews/{id}` Actualizar una reseña específica para un restaurante (IsClient).
- [ ] `DELETE /restaurants/{id}/reviews/{id}` Eliminar una reseña específica para un restaurante (IsClient).

## Blogs [OK]

- [x] `GET /posts` Obtener una lista de todos los posts (AllowAny).
- [x] `POST /posts` Crear un nuevo post (IsMarketing).
- [x] `GET /posts/{id}` Obtener los detalles de un post específico por su ID (AllowAny).
- [x] `PATCH /posts/{id}` Actualizar un post específico por su ID (IsMarketing).
- [x] `DELETE /posts/{id}` Eliminar un post específico por su ID (IsMarketing).

- [x] `POST /posts/{id}/report` Reportar un post específico por su ID (IsClient).
- [ ] `GET /posts/tags` Obtener una lista de todas las etiquetas (IsMarketing).
- [ ] `POST /posts/tags` Crear una nueva etiqueta (IsMarketing).

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

## Locations [OK]

- [x] `GET /countries` Obtener la lista de todos los países.
- [x] `POST /countries` Registrar un nuevo país.
- [x] `GET /countries/{id}` Obtener los detalles de un país específico.
- [x] `PUT /countries/{id}` Actualizar los detalles de un país específico.
- [x] `DELETE /countries/{id}` Eliminar un país específico.

- [x] `GET /states` Obtener la lista de todos los estados.
- [x] `POST /states` Registrar un nuevo estado.
- [x] `GET /states/{id}` Obtener los detalles de un estado específico.
- [x] `PUT /states/{id}` Actualizar los detalles de un estado específico.
- [x] `DELETE /states/{id}` Eliminar un estado específico.

- [x] `GET /cities` Obtener la lista de todas las ciudades.
- [x] `POST /cities` Registrar una nueva ciudad.
- [x] `GET /cities/{id}` Obtener los detalles de una ciudad específica.
- [x] `PUT /cities/{id}` Actualizar los detalles de una ciudad específica.
- [x] `DELETE /api/v1/cities/{id}` Eliminar una ciudad específica.

## Users [OK]

- [x] `GET /accounts/reviews` Obtener todas las reseñas escritas por un usuario específico (IsClient).
- [x] `GET /accounts/orders` Obtener todas las reseñas escritas por un usuario específico (IsClient).
- [x] `GET /accounts/{id}/historical` Obtener el historial de cambios de un usuario específico (IsAdministrator).

TODO: Agregar reviews a restaurants y posts, limitar modelo de Review

## Logica de Negocios

- [ ] El conductor tendrá un total de 50 puntos si no hace las entregas asignadas se ira descontando este porcentaje, si baja hasta 25 puntos que cambie el estado a ALERT, si baja mas de 10 se elimina la cuenta y se desvincula al driver
- [ ] Al actualizar el estado de una entrega, se podría validar que solo se pueda cambiar a estados específicos y que la fecha de entrega no haya pasado.
- [ ] Cuando se crea una compra, se crea un registro en el modelo Order y se establece el estado de pago como pendiente (payment_status=False).
- [ ] Una vez que el usuario realiza el pago, el estado de pago de la compra se actualiza a pagado (payment_status=True). Este paso puede realizarse a través de un sistema de pagos en línea o algún otro método de confirmación de pago.
- [ ] Cuando el pago se confirma, se activa la entrega asociada a la compra. Esto podría implicar la creación de un registro en el modelo Delivery y la asignación de un conductor para la entrega.
