import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add2(1, -5)
        self.assertEqual(result, "Wrong Input")
    def test_sub(self):
        result = calc.sub2(5, 2)
        self.assertEqual(result, 3)
    def test_pro(self):
        result = calc.pro2(1, 3)
        self.assertEqual(result, 3)

    
if __name__ == '__main__':
    unittest.main()

