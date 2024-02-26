import sys, os

tokens_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tokens'))
sys.path.append(tokens_path)

from token_factory import TokenFactory

class Lexer:
    # language specific characters
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["make"]
    boolean = ["and", "or", "not"]
    comparisons = [">", "<", ">=", "<=", "?="]
    specialCharacters = "><=?"
    reserved = ["if", "elif", "else", "do", "while"]

    # Constructor
    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = None
        self.token = None

    # Tokenization
    def tokenize(self):  
        while self.idx < len(self.text):            
            self.char = self.text[self.idx]
            
            if self.char in self.digits:
                self.token = self.extract_number()
            elif self.char in self.letters:
                self.token = self.extract_word()
            elif self.char in self.operations:
                self.token = TokenFactory.operation(self.char)
            elif self.char in self.specialCharacters:
                comparison_operator = self.extract_special()
                self.token = TokenFactory.comparison(comparison_operator)
            else:
                self.move()
                continue

            self.move()
            self.tokens.append(self.token)

    # Extract Number
    def extract_number(self):
        number = ""
        is_float = False
        while (self.char in self.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                is_float = True
            number += self.char
            self.move()

        return TokenFactory.float(number) if is_float else TokenFactory.integer(number)

    # Extract Word
    def extract_word(self):
        word = ""
        while self.char in self.letters and self.idx < len(self.text):
            word += self.char
            self.move()
        
        if word in self.declarations:
            return TokenFactory.declaration(word)
        elif word in self.boolean:
            return TokenFactory.boolean(word)
        elif word in self.reserved:
            return TokenFactory.reserved(word)
        else:
            return TokenFactory.variable(word)     

    # Extract Special
    def extract_special(self):
        comparison_operator = ""
        while self.char in self.specialCharacters and self.idx < len(self.text):
            comparison_operator += self.char
            self.move()
        return comparison_operator

    # Moving the characters
    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]