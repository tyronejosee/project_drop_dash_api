# Example Request

```http
POST /api/orders/pay/
Content-Type: application/json
Authorization: Bearer TOKEN
```

```json
{
  "order_id": "d09c5311-7f56-494d-abb6-2774286f45e2",
  "token": "YOUR_CARD_TOKEN",
  "payment_method_id": "visa",
  "installments": 1,
  "issuer_id": "1234"
}
```
