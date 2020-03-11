"""Vigenere cipher"""
import string
from collections import defaultdict
from pprint import pprint


class Vigenere():
    """Vigenere class"""

    def __init__(self, key, message=''):
        self._MATRIX = self._build_matrix()
        self.message = message
        self.key = key

    @property
    def key(self):
        """Get key."""
        return self.__key

    @key.setter
    def key(self, key):
        """Set key of the vigenere, using upper case and removing spaces"""
        self.__key = "".join(key.upper().split())
        self.__filler_key = self._build_filler_key()

    @property
    def message(self):
        """Get message."""
        return self.__message

    @message.setter
    def message(self, message):
        """Set message, setting upper case and removing non alpha keys."""
        self.__message = "".join(
            (letter.upper() for letter in message if letter in string.ascii_letters))

    def _build_matrix(self):
        """Build the shifting alphabet matrix lookup table"""
        """
        A B C D E F
        B C D E F G
        C D E F G H
        D E F G H I
    
        """
        matrix = defaultdict(dict)
        x = 0
        shifting_letters = string.ascii_uppercase
        for col in string.ascii_uppercase:
            for row in string.ascii_uppercase:
                matrix[col][row] = shifting_letters[x]
                x += 1
            # shift the alphabet by one
            shifting_letters = shifting_letters[1:] + shifting_letters[0]
            x = 0

        # pprint(matrix)
        # print(matrix['C']['C'])
        return matrix

    def _build_filler_key(self):
        """Key has to be same length as message, if not, repeat key until it is"""
        filler_key = ''
        # the __key has to be same length as __message
        if len(self.__key) >= len(self.__message):
            filler_key = self.__key[:len(self.__message)]
        else:
            while len(filler_key) < len(self.__message):
                filler_key += self.__key
            filler_key = filler_key[:len(self.__message)]
        return filler_key

    def _print_info(self):
        """Print info about the current data"""
        print(f"Message = {self.message}")
        print(f"Key = {self.key}")
        print(f"Filler key: {self.__filler_key}")

    def encrypt_message(self):
        """Encrypt message using key in the lookup matrix"""

        print("\nEncrypting")
        self._print_info()

        # for each letter in __message is column and __key as row in the matrix
        encrypted_message = ''
        for index, col in enumerate(self.__message):
            row = self.__filler_key[index]
            encrypted_message += self._MATRIX[col][row]
        return self._chunk_string(5, encrypted_message)

    def decrypt_message(self):
        """Decrypt message using key in the lookup matrix"""
        print("\nDecrypting")
        self._print_info()

        plaintext = ''
        # knowing the value and __key, we need to get the column
        for index, letter in enumerate(self.__message):
            # find the column where row and value is known
            for row_key, row_value in self._MATRIX.items():
                for col_key, col_value in row_value.items():
                    if col_value == letter and col_key == self.__filler_key[index]:
                        plaintext += row_key
                        # print(f"{row_key=}, {col_key=} {col_value=}")
                        break
        return plaintext

    def _chunk_string(self, size, string):
        """Break a string up into chunks of size"""
        chars, chunk_size = len(string), size
        return ' '.join([string[i:i + chunk_size] for i in range(0, chars, chunk_size)])


def test(testasdf='adf'):
    print(testasdf)


def main():
    test()
    message = 'SPEAK FRIEND AND ENTER'
    key = 'BAGGINS'
    vig = Vigenere(key, message)

    encrypted_message = vig.encrypt_message()
    print(f"Encrypted message = {encrypted_message}")

    vig.message = 'TPKGS SJJETJ IAV FNZKZ'
    vig.key = 'BAGGINS'
    print(f"Decrypted message = {vig.decrypt_message()}")

    # vig.message = encrypted_message
    # decrypted_message = vig.decrypt_message()
    # print(f"Decrypted message = {decrypted_message}")


if __name__ == '__main__':
    main()
