import unittest
import Function 
class TestMorseCode(unittest.TestCase):

    # def test_encryption(self):
    #     # from Function import encryption  
    #     text = "HELLO WORLD"
    #     expected_result = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    #     self.assertEqual(Function.encryption(text), expected_result)

    def test_encryption_all_uppercase(self):
        self.assertEqual(Function.encryption("HELLO WORLD"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    # def test_encryption_all_lowercase(self):
    #     self.assertEqual(square.calculate_square(1.5),2.25)

    # def test_zero(self):
    #     self.assertEqual(square.calculate_square(0),0)
    
    # def test_invalid_number(self):
    #     self.assertRaises(ValueError,square.calculate_square,"ab")


if __name__ == '__main__':

    unittest.main()
