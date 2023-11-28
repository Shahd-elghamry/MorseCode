import unittest
import Function 
class TestMorseCode(unittest.TestCase):


    def test_encryption_all_uppercase(self):
        self.assertEqual(Function.encryption("HELLO WORLD"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_all_lowercase(self):
        self.assertEqual(Function.encryption("hello world"),".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encryption_with_numbers(self):
        self.assertEqual(Function.encryption("H3ll0 W0r1d"),".... ...-- .-.. .-.. ----- / .-- ----- .-. .---- -..")

    def test_encryption_Characters_alphabet_numbers(self):
        self.assertEqual(Function.encryption("H3ll0-W0r1d!!!"),".... ...-- .-.. .-.. ----- -....- .-- ----- .-. .---- -.. -.-.-- -.-.-- -.-.--")
    
    def test_encryption_with_numbers_characters(self):
        self.assertEqual(Function.encryption("2023@1234--"),"..--- ----- ..--- ...-- .--.-. .---- ..--- ...-- ....- -....- -....-")

    def test_decryption_without_space(self):
        self.assertEqual(Function.decryption(".... .."), "HI")
    
    def test_decryption_with_spaces(self):
        self.assertEqual(Function.decryption(".... .. / -- -.-- / -. .- -- . / .. ... / ... .... .- .... -.."), "HI MY NAME IS SHAHD")
    
    def test_invalid_input(self):
        self.assertAlmostEqual(Function.invalid_input(""),"Invalid input. Please enter a valid option." )


if __name__ == '__main__':

    unittest.main()
