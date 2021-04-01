import unittest

example = __import__('01_01_example')
 
class Test(unittest.TestCase):
    def test_case_1(self):
        c = example.solution(20, 10)
        self.assertEqual(c, 30)
 
 
if __name__ == '__main__':
    unittest.main()