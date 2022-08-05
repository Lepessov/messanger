from django.utils.timezone import now
from rest_framework.test import APITestCase

from ..models import MailSender, Client, Message


class TestModel(APITestCase):

    def maile_sender_test(self):
        mailing = MailSender.objects.create(start_day="2022-08-04T09:55:27Z", end_day="2024-08-04T09:55:27Z", body='Something',
                                         start_time="18:00:00", end_time="19:00:00", tag='Daulet',
                                         )
        self.assertIsInstance(mailing, MailSender)
        self.assertEqual(mailing.tag, 'Daulet')

    def client_create_test(self):
        client = Client.objects.create(number='71234567890', operator_code='123',
                                       tag='Daulet', timezone='UTC/Arizone')
        self.assertIsInstance(client, Client)
        self.assertEqual(client.number, '71234567890')

    def message_create_test(self):
        self.test_creates_mailings()
        self.test_creates_clients()
        message = Message.objects.create(status='No sent', mail_sender_id=1, client_id=1)
        self.assertIsInstance(message, Message)
        self.assertEqual(message.status, 'No sent')