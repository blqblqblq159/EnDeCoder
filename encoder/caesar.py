from base import *
import random
import re

class CaesarEncoder(Encoder):

    def __init__(self, text_to_encode = None, rotation = 0):
        super().__init__(text_to_encode)
        self.rotation = rotation
    
    @property
    def encoded_text(self):
        pattern = '|'.join(sorted(k for k in self.encoder_alphabet))
        return re.sub(pattern, lambda m: self.encoder_alphabet.get(m.group(0)), self.text)

        # encoded_text = ""
        # for char in self.text:
        #     if char in self.encoder_alphabet.keys():
        #         encoded_text += self.encoder_alphabet[char]
        #     else:
        #         encoded_text += char
        # return encoded_text
    
    @property
    def encoder_alphabet(self):
        alphabet_encode = {}
        for k, v in self.alphabet_num_str.items():
            alphabet_encode[v] = self.alphabet_num_str[(k + self.rotation) % 26]
        return alphabet_encode
    
    def rotate_right(self, amount = 1):
        self.rotation -= amount

    def rotate_left(self, amount = 1):
        self.rotation += amount

    def randomize(self):
        self.rotation = random.randint(0, 25)
        

if __name__ == '__main__':
    text = "veel succes met de encoder thing"
    rotation = 5
    test = CaesarEncoder(text, rotation)

    print(test.encoded_text)
    # test.rotate_left()
    # print(test.encoded_text)
    # print(test.encoder_alphabet)

        

    


    
