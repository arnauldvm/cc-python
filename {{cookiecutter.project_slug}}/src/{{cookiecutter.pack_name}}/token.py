from dataclasses import dataclass
import string
import secrets
import random
from math import log2


@dataclass
class AlphabetDefinition():
    use_upper: bool = True
    use_lower: bool = False
    use_digits: bool = True
    use_special: bool = False

    def get_chars(self) -> str:
        chars = ''
        if self.use_upper:
            chars += string.ascii_uppercase
        if self.use_lower:
            chars += string.ascii_lowercase
        if self.use_digits:
            chars += string.digits
        if self.use_special:
            chars += string.punctuation
        return chars


def generate(alphabet: AlphabetDefinition = AlphabetDefinition(), length: int = 12):
    characters = [secrets.choice(alphabet.get_chars()) for _ in range(length)]
    random.shuffle(characters)
    while characters[0] == ' ' or characters[-1] == ' ':
        # Avoid passwords starting or ending with space
        random.shuffle(characters)
    return ''.join(characters)


def compute_entropy(alphabet: AlphabetDefinition = AlphabetDefinition(), length: int = 12) -> float:
    return length * log2(len(alphabet.get_chars()))
    # This formula need confirmation


def get_strength_class(entropy: float) -> str:
    # from https://www.omnicalculator.com/other/password-entropy
    if entropy >= 128:
        return 'extremely strong'
    elif entropy >= 60:
        return 'very strong'
    elif entropy >= 36:
        return 'strong'
    elif entropy >= 28:
        return 'reasonable'
    elif entropy >= 18:
        return 'weak'
    else:
        return 'extremely weak'
