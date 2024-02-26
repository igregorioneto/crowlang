# Gerenciar as variáveis e suas atribuições
class Data:
    def __init__(self):
        self.variables = {}

    def read(self, variable_name):
        return self.variables.get(variable_name)
    
    def read_all(self):
        return self.variables
    
    def write(self, variable_name, value):
        self.variables[variable_name] = value