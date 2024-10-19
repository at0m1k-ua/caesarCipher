from unittest import TestCase

from Alphabet import Alphabet
from CaesarCipher import CaesarCipher


class CaesarCipherTest(TestCase):
    def test_caesar_cipher_encodes_and_decodes_as_expected_with_latin(self):
        input_str = 'Hello, world'
        shift = 7
        expected_str = 'Olssv, dvysk'  # https://cryptii.com/pipes/caesar-cipher

        self.__test_caesar_cipher_encodes_and_decodes_as_expected(input_str, expected_str, shift)

    def test_caesar_cipher_encodes_and_decodes_as_expected_with_ukrainian(self):
        input_str = 'Привіт, світ'
        shift = 4
        expected_str = 'Уфкелц, хелц'

        self.__test_caesar_cipher_encodes_and_decodes_as_expected(input_str, expected_str, shift)

    def __test_caesar_cipher_encodes_and_decodes_as_expected(self,
                                                             input_str: str,
                                                             expected_str: str,
                                                             shift: int):
        alphabet = Alphabet.load_from_json('../alphabet.json')
        caesar_cipher = CaesarCipher(alphabet)
        encoded_str = caesar_cipher.encrypt(input_str, shift)
        self.assertEqual(expected_str, encoded_str)

        decoded_str = caesar_cipher.decrypt(encoded_str, shift)
        self.assertEqual(input_str, decoded_str)
