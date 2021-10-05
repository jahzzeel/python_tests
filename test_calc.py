import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):

        self.assertEqual(calc.add(10,5),15)

    def test_divide(self):

        self.assertEqual(calc.divide(10,2),5)

        #print("Ddddddd")
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__== '__main__':
    unittest.main()
