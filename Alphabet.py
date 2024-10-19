import json


class Alphabet:
    def __init__(self, sequences):
        self.sequences = sequences

    @staticmethod
    def load_from_json(filepath: str):
        with open(filepath, 'r') as file:
            alphabets = json.load(file)
            return Alphabet(alphabets)

    def shift_char(self, char: str, step: int):
        if len(char) > 1:
            raise ValueError("Char should have length = 1")

        for case in self.sequences:
            if char in case:
                new_index = (case.index(char) + step) % len(case)
                return case[new_index]

        return char
