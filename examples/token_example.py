import sys, os

tokens_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tokens'))
sys.path.append(tokens_path)

from token_factory import TokenFactory

# Exemple of use:
integer_token = TokenFactory.integer(10)
float_token = TokenFactory.float(3.14)
operation_token = TokenFactory.operation("+")
declaration_token = TokenFactory.declaration("make")
variable_token = TokenFactory.variable("x")
boolean_token = TokenFactory.boolean("and")
comparison_token = TokenFactory.comparison(">")
reserved_token = TokenFactory.reserved("if")

print(integer_token)
print(float_token)
print(operation_token)
print(declaration_token)
print(variable_token)
print(boolean_token)
print(comparison_token)
print(reserved_token)