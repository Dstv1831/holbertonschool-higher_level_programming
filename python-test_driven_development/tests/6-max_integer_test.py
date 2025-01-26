import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

     """Define unittests for max_integer([..])."""
     
     def test_max_at_the_end(self):
          """Test a list with a max value in the last element"""
          max_at_end = [1, 2, 3, 4]
          self.assertEqual(max_integer(max_at_end), 4)
          
     if __name__ == '__main__':
          unittest.main()