import unittest
import Function 
class TestMorseCode(unittest.TestCase):

    def test_encryption(self):
        from Function import encryption  # Replace 'your_module' with the actual module name
        text = "HELLO WORLD"
        expected_result = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        self.assertEqual(encryption(text), expected_result)

    def test_negative_number(self):
        self.assertEqual(square.calculate_square(-3),9)

    def test_decimal_number(self):
        self.assertEqual(square.calculate_square(1.5),2.25)

    def test_zero(self):
        self.assertEqual(square.calculate_square(0),0)
    
    def test_invalid_number(self):
        self.assertRaises(ValueError,square.calculate_square,"ab")


if __name__ == '__main__':

    unittest.main()
