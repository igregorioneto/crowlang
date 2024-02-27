class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx] 

    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token
        elif self.token.value == "(":
            self.move()
            return self.boolean_expression()
        elif self.token.value == "not":
            operator = self.token
            self.move()
            return [operator, self.boolean_expression()]
        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            return [operator, self.boolean_expression()]
        
    def term(self):
        left_node = self.factor()
        self.move()

        while self.token.value in {"*", "/"}:
            operator = self.token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, operator, right_node]

        return left_node
    
    def if_statement(self):
        self.move()
        condition = self.boolean_expression()

        if self.token.value == "do":
            self.move()
            action = self.statement()
            return condition, action
        elif self.tokens[self.idx - 1].value == "do":
            action = self.statement()
            return condition, action
    
    def if_statements(self):
        conditions = []
        actions = []
        if_statement = self.if_statement()

        conditions.append(if_statement[0])
        actions.append(if_statement[1])

        while self.token.value == "elif":
            if_statement = self.if_statement()
            conditions.append(if_statement[0])
            actions.append(if_statement[1])
        
        if self.token.value == "else":
            self.move()
            self.move()
            else_action = self.statement()
            return [conditions, actions, else_action]
        
        return [conditions, actions]
    
    def while_statement(self):
        self.move()
        condition = self.boolean_expression()

        if self.token.value == "do":
            self.move()
            action = self.statement()
            return [condition, action]
        elif self.tokens[self.idx - 1].value == "do":
            action = self.statement()
            return [condition, action]
        

    def comp_expression(self):
        left_node = self.expression()
        while self.token.type == "COMP":
            operator = self.token
            self.move()
            right_node = self.expression()
            left_node = [left_node, operator, right_node]
        return left_node
    
    
        

