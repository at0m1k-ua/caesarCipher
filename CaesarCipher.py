from Alphabet import Alphabet


class CaesarCipher:
    def __init__(self, alphabet: Alphabet):
        self.__alphabet = alphabet

    def encode(self, input_str: str, shift: int):
        return self.__shift(input_str, shift)

    def decode(self, input_str: str, shift: int):
        return self.__shift(input_str, -shift)

    def __shift(self, input_str: str, shift: int):
        output_str = ''
        for ch in input_str:
            output_str += self.__alphabet.shift_char(ch, shift)

        return output_str
