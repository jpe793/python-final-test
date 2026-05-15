import unittest
from unique_code import unique_code

class TestUniqueCode(unittest.TestCase):
    def test_alex(self):
        self.assertEqual(unique_code("Alex"), "65108101120")

if __name__ == "__main__":
    unittest.main()