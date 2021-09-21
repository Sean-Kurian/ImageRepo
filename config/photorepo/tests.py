from django.test import TestCase
import unittest

# Create your tests here.
class APITests(unittest.TestCase): 
    def test_1(self): 
        self.assertEqual(5, 5)
        self.assertEqual(6, 6)

    def test_2(self): 
        self.assertEqual(5, 5)
        self.assertEqual(6, 6)