# Endpoints

## Todo

### Coupons

- [ ] `GET /api/coupons/`
- [ ] `POST /api/coupons/`
- [ ] `GET /api/coupons/{id}/`
- [ ] `PUT /api/coupons/{id}/`
- [ ] `DELETE /api/coupons/{id}/`
- [ ] `GET /api/coupons/active/`
- [ ] `POST /api/orders/{order_id}/apply-coupon/`
- [ ] `GET /api/coupons/{coupon_id}/orders/`
- [ ] `GET /api/coupons/{coupon_id}/total-discount/`

### Orders

- `GET /api/orders/`
- `POST /api/orders/`
- `GET /api/orders/{id}/`
- `PUT /api/orders/{id}/`
- `DELETE /api/orders/{id}/`
- `GET /api/users/{user_id}/orders/`
- `GET /api/restaurants/{restaurant_id}/orders/`
- `GET /api/orders/pending/`
- `GET /api/orders/completed/`
- `PUT /api/orders/{id}/update-status/`

**Logica de negocio**:

- Cuando se crea una compra, se crea un registro en el modelo Order y se establece el estado de pago como pendiente (payment_status=False).

- Una vez que el usuario realiza el pago, el estado de pago de la compra se actualiza a pagado (payment_status=True). Este paso puede realizarse a través de un sistema de pagos en línea o algún otro método de confirmación de pago.

- Cuando el pago se confirma, se activa la entrega asociada a la compra. Esto podría implicar la creación de un registro en el modelo Delivery y la asignación de un conductor para la entrega.

### Drivers

- `GET /api/drivers/`
- `POST /api/drivers/`
- `GET /api/drivers/{id}/`
- `PUT /api/drivers/{id}/`
- `DELETE /api/drivers/{id}/`
- `GET /api/drivers/{id}/orders/`
- `POST /api/drivers/{id}/orders/`
- `GET /api/drivers/{driver_id}/orders/{order_id}/`
- `PUT /api/drivers/{driver_id}/orders/{order_id}/`
- `DELETE /api/drivers/{driver_id}/orders/{order_id}/`

**Logica de negocio**:

- el conductor tendrá un total de 50 puntos si no hace las entregas asignadas se ira descontando este porcentaje, si baja hasta 25 puntos que cambie el estado a ALERT, si baja mas de 10 se elimina la cuenta y se desvincula al driver

- Al actualizar el estado de una entrega, se podría validar que solo se pueda cambiar a estados específicos y que la fecha de entrega no haya pasado.

### Payments

- `POST /api/payments`
- `GET /api/payments/{payment_id}`

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

1. Obtener todas las entregas:
   - `GET /api/deliveries/`

2. Crear una nueva entrega:
   - `POST /api/deliveries/`

3. Obtener detalles de una entrega específica:
   - `GET /api/deliveries/{id}/`

4. Actualizar detalles de una entrega específica:
   - `PUT /api/deliveries/{id}/`

5. Eliminar una entrega específica:
   - `DELETE /api/deliveries/{id}/`

6. Obtener todas las entregas para un pedido específico:
   - `GET /api/orders/{order_id}/deliveries/`

7. Crear una nueva entrega para un pedido específico:
   - `POST /api/orders/{order_id}/deliveries/`

8. Obtener detalles de una entrega específica para un pedido específico:
   - `GET /api/orders/{order_id}/deliveries/{delivery_id}/`

9. Actualizar detalles de una entrega específica para un pedido específico:
   - `PUT /api/orders/{order_id}/deliveries/{delivery_id}/`

10. Eliminar una entrega específica para un pedido específico:
    - `DELETE /api/orders/{order_id}/deliveries/{delivery_id}/`

### Done

### Restaurants

- [x] `GET /api/restaurants/`
- [x] `POST /api/restaurants/`
- [x] `GET /api/restaurants/{restaurant_id}/`
- [x] `PUT /api/restaurants/{restaurant_id}/`
- [x] `DELETE /api/restaurants/{restaurant_id}/`
- [x] `GET /api/restaurants/{restaurant_id}/foods/`
- [x] `POST /api/restaurants/{restaurant_id}/foods/`
- [x] `GET /api/restaurants/{restaurant_id}/foods/{food_id}/`
- [x] `PUT /api/restaurants/{restaurant_id}/foods/{food_id}/`
- [x] `DELETE /api/restaurants/{restaurant_id}/foods/{food_id}/`
