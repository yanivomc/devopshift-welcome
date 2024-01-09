import unittest
import unittest.mock
from code.messages import greet, farewell

class TestMessages(unittest.TestCase):
    
    def test_greet(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            returned_value = greet("Alice")
            mock_print.assert_called_with("Hello, Alice!")
            self.assertEqual(returned_value, "Hello, Alice!1")

    def test_farewell(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            returned_value = farewell("Bob")
            mock_print.assert_called_with("Goodbye, Bob!")
            self.assertEqual(returned_value, "Goodbye, Bob!")

if __name__ == '__main__':
    unittest.main()
