import t2
import unittest

class MyTest(unittest.TestCase) :

    def test_even(self) :
        self.assertEqual(t2.checknum(2),"Even")
        self.assertNotEqual(t2.checknum(2),"Odd")

    def test_odd(self) :
        self.assertNotEqual(t2.checknum(1),"Even")
        self.assertEqual(t2.checknum(1),"Odd")

if __name__ == '__main__' :
    unittest.main()
