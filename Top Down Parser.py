import re

def tokenize(expression):
    token_specification = [
        ('NUMBER',   r'\d+'),          # Integer number
        ('PLUS',     r'\+'),           # Addition operator
        ('TIMES',    r'\*'),           # Multiplication operator
        ('LPAREN',   r'\('),           # Left parenthesis
        ('RPAREN',   r'\)'),           # Right parenthesis
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
    ]
    
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    get_token = re.compile(token_regex).match
    line = expression.strip()
    tokens = []
    pos = 0
    match = get_token(line)
    
    while match:
        kind = match.lastgroup
        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(match.group(kind))))
        elif kind in ('PLUS', 'TIMES', 'LPAREN', 'RPAREN'):
            tokens.append((kind, match.group(kind)))
        elif kind == 'SKIP':
            pass
        else:
            raise SyntaxError(f'Unexpected character: {line[pos]}')
        
        pos = match.end()
        match = get_token(line, pos)
    
    return tokens
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        """
        Advance to the next token.
        """
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def parse(self):
        """
        Parse the expression starting from the 'E' non-terminal.
        """
        result = self.expr()
        if self.current_token is not None:
            raise SyntaxError('Unexpected token at the end')
        return result

    def expr(self):
        """
        E -> T + E | T
        """
        result = self.term()
        while self.current_token and self.current_token[0] == 'PLUS':
            self.next_token()
            result += self.term()
        return result

    def term(self):
        """
        T -> F * T | F
        """
        result = self.factor()
        while self.current_token and self.current_token[0] == 'TIMES':
            self.next_token()
            result *= self.factor()
        return result

    def factor(self):
        """
        F -> ( E ) | num
        """
        if self.current_token[0] == 'NUMBER':
            value = self.current_token[1]
            self.next_token()
            return value
        elif self.current_token[0] == 'LPAREN':
            self.next_token()
            result = self.expr()
            if self.current_token[0] != 'RPAREN':
                raise SyntaxError('Expected closing parenthesis')
            self.next_token()
            return result
        else:
            raise SyntaxError('Unexpected token')

expression = "2 + 3 * (4 + 5)"
tokens = tokenize(expression)
parser = Parser(tokens)
result = parser.parse()
print(f"Result: {result}") 
