import unittest
from src.sample import Sample

class SampleMethods(unittest.TestCase):
    def setUp(self):
        self.sample = Sample()
    
    def test_add(self):
        self.assertEqual(self.sample.add(10), 20)
    
    def test_get_a(self):
        self.assertEqual(self.sample.get_a(), 10)
    
    