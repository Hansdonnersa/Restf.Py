from django.test import TestCase
from django.urls import reverse, resolve
from ..views import SumView, AverageView

class UrlTests(TestCase):
    def test_sum_url(self):
        url = reverse('sum')
        self.assertEqual(resolve(url).func.view_class, SumView)

    def test_average_url(self):
        url = reverse('average')
        self.assertEqual(resolve(url).func.view_class, AverageView)