import unittest
import Function 
class TestMorseCode_Encryption(unittest.TestCase):

    # def test_encryption(self):
    #     # from Function import encryption  
    #     text = "HELLO WORLD"
    #     expected_result = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    #     self.assertEqual(Function.encryption(text), expected_result)

    def test_encryption_all_uppercase(self):
        self.assertEqual(Function.encryption("HELLO WORLD"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_all_lowercase(self):
        self.assertEqual(Function.encryption("hello world"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_with_numbers(self):
        self.assertEqual(Function.encryption("H3ll0 W0r1d"),".... ...-- .-.. .-.. ----- / .-- ----- .-. .---- -..")
    


if __name__ == '__main__':

    unittest.main()
