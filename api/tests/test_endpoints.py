from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class SumViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('sum')

    def test_sum_valid_data(self):
        data = {'numbers': [1, 2, 3, 4, 5]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sum'], 15)

    def test_sum_empty_list(self):
        data = {'numbers': []}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('numbers', response.data)

    def test_sum_invalid_data(self):
        data = {'numbers': [1, 2, "a", 4, 5]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('numbers', response.data)


class AverageViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('average')

    def test_average_valid_data(self):
        data = {'numbers': [10, 20, 30, 40, 50]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average'], 30)

    def test_average_empty_list(self):
        data = {'numbers': []}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('numbers', response.data)

    def test_average_invalid_data(self):
        data = {'numbers': [10, 20, "a", 40, 50]}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('numbers', response.data)