from django.test import TestCase, override_settings
from unittest.mock import patch, MagicMock
from django.contrib.auth import get_user_model
from products.models import Product, Order
from billing.models import Payment
from rest_framework.test import APIClient
from django.urls import reverse


User = get_user_model()

@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class PaymentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # self.user = User.objects.create_user(username="ali", password="1234")
        self.user = User.objects.create_user(id=1, phone_number='+998901234567', password='testpass')
        self.product = Product.objects.create(name="Olma", price=10.00)
        self.order = Order.objects.create(
            product=self.product,
            customer=self.user,
            quantity=2,
            is_paid=False
        )
        self.url = reverse("create-charge")

    # @patch("products.signals.send_telegram_notification.delay")  # Redis signalni bloklaydi
    @patch("stripe.Charge.create")  # Stripe API chaqirilmaydi
    def test_create_payment_success(self, mock_stripe_charge):
        """
        Stripe orqali muvaffaqiyatli to‘lov test
        """
        # Stripe javobini soxtalashtiramiz
        mock_stripe_charge.return_value = {"id": "ch_123456789"}

        payload = {
            "stripe_token": "tok_test_123",
            "order_id": self.order.id
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "Payment successful")

        # Payment DB da yaratilganini tekshirish
        payment = Payment.objects.get(order=self.order)
        self.assertEqual(payment.amount, self.order.product.price * self.order.quantity)
        self.assertEqual(payment.stripe_charge_id, "ch_123456789")

        # Order to‘langan holatga o‘tganini tekshirish
        self.order.refresh_from_db()
        self.assertTrue(self.order.is_paid)

        # Telegram signal chaqirilganini tekshirish
        # mock_telegram.assert_called_once()
