# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from billing.models import Payment
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# import os, django
#
# User = get_user_model()
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
#
# class PaymentTests(APITestCase):
#     # python manage.py dumpdata billing.Payment --format=yaml --indent=4 > billing/fixtures/Payments.yaml
#     # fixtures = ['Payments', 'orders']
#     fixtures = ['billing/fixtures/products.yaml', 'billing/fixtures/orders.yaml', 'billing/fixtures/Payments.yaml']
#
#     def setUp(self):
#         self.user = User.objects.create_user(id=1, phone_number='+998901234567', password='testpass')
#         self.client.force_authenticate(user=self.user)
#         self.payment1 = Payment.objects.first()
#
#     def test_Payment_list(self):
#         url = reverse('Payment-list')
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(len(response.data), 4)
#
