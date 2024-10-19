from unittest import TestCase

from Alphabet import Alphabet


class AlphabetTest(TestCase):
    def test_alphabets_set_shifts_chars(self):
        input_str = 'AbCdE123fg'
        expected_str = 'CdEaB123fg'

        actual_str = ''
        alphabet = Alphabet(['abcde', 'ABCDE'])
        for ch in input_str:
            actual_str += alphabet.shift_char(ch, 2)

        self.assertEqual(expected_str, actual_str)

    def test_alphabet_is_loaded_from_json(self):
        path = '../alphabet.json'
        alphabet = Alphabet.load_from_json(path)
        self.assertGreater(len(alphabet.sequences), 0)
