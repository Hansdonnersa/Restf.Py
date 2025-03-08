from django.test import TestCase
from ..serializers import VectorSerializer

class VectorSerializerTests(TestCase):
    def test_valid_data(self):
        data = {'numbers': [1, 2, 3, 4, 5]}
        serializer = VectorSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_empty_list(self):
        data = {'numbers': []}
        serializer = VectorSerializer(data=data)
        self.assertFalse(serializer.is_valid())  
        self.assertIn('numbers', serializer.errors)  

    def test_invalid_data(self):
        data = {'numbers': [1, 2, "a", 4, 5]}
        serializer = VectorSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('numbers', serializer.errors)