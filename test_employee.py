import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):


    


    @classmethod
    def setUpClass(cls):
        print("SETUP")
        cls.emp_1 = Employee('corey', 'Schafer', 5000)

    # def setUp(self):
    #    print("SETUP")
    #    self.emp_1=Employee('corey','Schafer',5000)

    def test_email(self):
        print("//////")
        self.assertEqual(self.emp_1.email, 'corey.Schafer@email.com')

    def test_apply_rise(self):
        print("======")
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 5250.00)


if __name__ == '__main__':
    unittest.main()
