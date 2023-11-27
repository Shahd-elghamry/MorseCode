import unittest
import Function 
class TestMorseCode_Encryption(unittest.TestCase):


    def test_encryption_all_uppercase(self):
        self.assertEqual(Function.encryption("HELLO WORLD"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_all_lowercase(self):
        self.assertEqual(Function.encryption("hello world"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_with_numbers(self):
        self.assertEqual(Function.encryption("H3ll0 W0r1d"),".... ...-- .-.. .-.. ----- / .-- ----- .-. .---- -..")

    def test_encryption_Characters_alphabet_numbers(self):
        self.assertEqual(Function.encryption("H3ll0-W0r1d!!!"),".... ...-- .-.. .-.. ----- -....- .-- ----- .-. .---- -.. -.-.-- -.-.-- -.-.--")
    
    def test_encryption_with_numbers_characters(self):
        self.assertEqual(Function.encryption("2023@1234--"),"")


if __name__ == '__main__':

    unittest.main()
