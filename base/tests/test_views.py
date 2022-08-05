from django.utils.timezone import now
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import MailSender, Message, Client


class TestStat(APITestCase):


    def test_mailSender(self):
        local_host = "http://127.0.0.1:8000"
        dict = {
            "start_day": "2022-08-04T09:55:27Z", 
            "end_day": "2024-08-04T09:55:27Z", 
            'start_time': "18:00:00",
            'end_time': "19:00:00", 
            "body": "Something", 
            "tag": "Daulet",
            "operator_code": '123'
        }
        create_mailSender = dict
        resp = self.client.post(f'{local_host}/api/create/mailing', create_mailSender)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['body'], 'Something')
        self.assertIsInstance(resp.data['body'], str)

    def client_test(self):
        local_host = "http://127.0.0.1:8000"
        dict = {
            "number": '8771332121983',
            "tag": "Daulet", 
            "timezone": "UTC", 
            "operator_code": "123"
        }
        create_client = dict
        resp = self.client.post(f'{local_host}/api/create/client', create_client)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['number'], '8771332121983')
        self.assertIsInstance(resp.data['number'], str)

    def test_message(self):
        local_host = "http://127.0.0.1:8000"
        response = self.client.get(f'{local_host}/api/messages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
