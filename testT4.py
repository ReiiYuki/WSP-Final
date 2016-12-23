import t4
import unittest

class MyTest(unittest.TestCase) :

    def teststamp7(self) :
        self.assertEqual(t4.stamp7(30),[0,0])
        self.assertEqual(t4.stamp7(40),[1,0])
        self.assertEqual(t4.stamp7(120),[0,1])
        self.assertEqual(t4.stamp7(160),[1,1])
        #[Stamp-1B, Stamp-3B]

    def testmembercheck(self) :
        self.assertTrue(t4.memberCheck('1234')=='You are a member')
        self.assertTrue(t4.memberCheck('1234')!='You are not a member')
        self.assertTrue(t4.memberCheck('12345')=='You are not a member')
        self.assertTrue(t4.memberCheck('12345')!='You are a member')

if __name__ == '__main__':
    unittest.main()
