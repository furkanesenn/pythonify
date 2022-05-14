import unittest
import check_code

class TestPythonify(unittest.TestCase):

    def test_check_code(self):
        result = check_code.check_code(r'C:\Users\furfatsev\Desktop\[general]\.py\pythonify\test_cases\script.py')
        print(result)
        self.assertIsNotNone(result,)