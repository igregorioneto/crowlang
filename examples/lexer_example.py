import os, sys

lexes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lexes'))
sys.path.append(lexes_path)

from lexer_custom import Lexer

# Example of use
print("Example 1: ")
text = "make x = 10"
lexer_custom = Lexer(text)
lexer = lexer_custom.tokenize()
print(f"{lexer_custom.tokens}\n")

print("Example 2: ")
text = "make y = false"
lexer_custom = Lexer(text)
lexer = lexer_custom.tokenize()
print(f"{lexer_custom.tokens}\n")

print("Example 3: ")
text = "make z = 10 + 5"
lexer_custom = Lexer(text)
lexer = lexer_custom.tokenize()
print(f"{lexer_custom.tokens}\n")
