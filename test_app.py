# test_app.py

import unittest
from app import bonjour

class TestApp(unittest.TestCase):
 def test_bonjour(self):
    self.assertEqual(bonjour("Jenkins"), "Bonjour Jen  kins !")
    self.assertEqual(bonjour("CI"), "Bonjour CI !")

if __name__ == "__main__":
 unittest.main()