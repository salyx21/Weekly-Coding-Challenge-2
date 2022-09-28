import unittest
import disarium

class Testsolution(unittest.TestCase):
    def test_disarium_75(self):
        number = 75
        result = disarium.disarium(number)
        self.assertEqual(result,False)
    def test_disarium_135(self):
        number = 135
        result = disarium.disarium(number)
        self.assertEqual(result,True)
    def test_disarium_544(self):
        number = 544
        result = disarium.disarium(number)
        self.assertEqual(result,False)
    def test_disarium_518(self):
        number = 518
        result = disarium.disarium(number)
        self.assertEqual(result,True)
    def test_disarium_466(self):
        number = 466
        result = disarium.disarium(number)
        self.assertEqual(result,False)
    def test_disarium_8(self):
        number = 8
        result = disarium.disarium(number)
        self.assertEqual(result,True)

