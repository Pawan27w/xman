import unittest

class Test_Company(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup method..")

    def test_Z(self):
        print("test method in z")

    def test_A(self):
        print("test method in A")

    def test_C(self):
        print("test method in c")
    @classmethod
    def tearDownClass(cls):
        print("Tear Down")

if __name__=="__main__":
    unittest.main()