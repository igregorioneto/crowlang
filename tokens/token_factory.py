from token_custom import Token

class TokenFactory:
    @staticmethod
    def integer(value):
        return Token("INT", value)
    
    @staticmethod
    def float(value):
        return Token("FLT", value)
    
    @staticmethod
    def operation(value):
        return Token("OP", value)
    
    @staticmethod
    def declaration(value):
        return Token("DECL", value)
    
    @staticmethod
    def variable(value):
        return Token("VAR(?)", value)
    
    @staticmethod
    def boolean(value):
        return Token("BOOL", value)
    
    @staticmethod
    def comparison(value):
        return Token("COMP", value)
    
    @staticmethod
    def reserved(value):
        return Token("RSV", value)