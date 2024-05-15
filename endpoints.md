# Endpoints

## Apps

### Posts

- [x] GET /api/posts/
- [x] POST /api/posts/
- [x] GET /api/posts/{id}/
- [x] PATCH /api/posts/{id}/
- [x] DELETE /api/posts/{id}
- [x] GET /api/posts/tags/
- [x] POST /api/posts/tags/
- [x] GET /api/posts/search/?q={query}

### Orders

- [ ] `GET /api/ordders/me`
- [ ] `GET /api/orders/`
- [ ] `POST /api/orders/`
- [ ] `GET /api/orders/{id}/`
- [ ] `PUT /api/orders/{id}/`
- [ ] `DELETE /api/orders/{id}/`
- [ ] `GET /api/orders/pending/`
- [ ] `GET /api/orders/completed/`

- `PUT /api/orders/{id}/update-status/`
- [ ] `POST /api/orders/{order_id}/apply-coupon/`

**Logica de negocio**:

- Cuando se crea una compra, se crea un registro en el modelo Order y se establece el estado de pago como pendiente (payment_status=False).

- Una vez que el usuario realiza el pago, el estado de pago de la compra se actualiza a pagado (payment_status=True). Este paso puede realizarse a través de un sistema de pagos en línea o algún otro método de confirmación de pago.

- Cuando el pago se confirma, se activa la entrega asociada a la compra. Esto podría implicar la creación de un registro en el modelo Delivery y la asignación de un conductor para la entrega.

### Drivers

- [x] `GET /api/drivers/`
- [x] `POST /api/drivers/`
- [x] `GET /api/drivers/{id}/`
- [x] `PUT /api/drivers/{id}/`
- [x] `DELETE /api/drivers/{id}/`
- [ ] `GET /api/drivers/{id}/orders/`
- [ ] `POST /api/drivers/{id}/orders/`
- [ ] `GET /api/drivers/{driver_id}/orders/{order_id}/`
- [ ] `PUT /api/drivers/{driver_id}/orders/{order_id}/`
- [ ] `DELETE /api/drivers/{driver_id}/orders/{order_id}/`

**Logica de negocio**:

- el conductor tendrá un total de 50 puntos si no hace las entregas asignadas se ira descontando este porcentaje, si baja hasta 25 puntos que cambie el estado a ALERT, si baja mas de 10 se elimina la cuenta y se desvincula al driver

- Al actualizar el estado de una entrega, se podría validar que solo se pueda cambiar a estados específicos y que la fecha de entrega no haya pasado.

### Payments

- [ ] `POST /api/payments`
- [ ] `GET /api/payments/{payment_id}`

### Promotions

- `GET /api/promotions/`
- `POST /api/promotions/`
- `GET /api/promotions/{id}/`
- `PUT /api/promotions/{id}/`
- `DELETE /api/promotions/{id}/`
- `GET /api/restaurants/{restaurant_id}/promotions/`
- `POST /api/restaurants/{restaurant_id}/promotions/`
- `GET /api/restaurants/{restaurant_id}/promotions/{promotion_id}/`
- `PUT /api/restaurants/{restaurant_id}/promotions/{promotion_id}/`
- `DELETE /api/restaurants/{restaurant_id}/promotions/{promotion_id}/`

### Deliveries

- [ ] `GET /api/deliveries/`
- [ ] `POST /api/deliveries/`
- [ ] `GET /api/deliveries/{id}/`
- [ ] `PUT /api/deliveries/{id}/`
- [ ] `DELETE /api/deliveries/{id}/`
- [ ] `GET /api/orders/{order_id}/deliveries/`
- [ ] `POST /api/orders/{order_id}/deliveries/`
- [ ] `GET /api/orders/{order_id}/deliveries/{delivery_id}/`
- [ ] `PUT /api/orders/{order_id}/deliveries/{delivery_id}/`
- [ ] `DELETE /api/orders/{order_id}/deliveries/{delivery_id}/`

### Coupons

- [x] `GET /api/coupons/`
- [x] `POST /api/coupons/`
- [x] `GET /api/coupons/{id}/`
- [x] `PUT /api/coupons/{id}/`
- [x] `DELETE /api/coupons/{id}/`
- [ ] `GET /api/coupons/{coupon_id}/orders/`

### Restaurants

- [x] `GET /api/restaurants/`
- [x] `POST /api/restaurants/`
- [x] `GET /api/restaurants/{restaurant_id}/`
- [x] `PUT /api/restaurants/{restaurant_id}/`
- [x] `DELETE /api/restaurants/{restaurant_id}/`
- [x] `GET /api/restaurants/{restaurant_id}/foods/`
- [ ] `GET /api/restaurants/{restaurant_id}/orders/`
