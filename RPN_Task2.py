class Token:
    def __init__(self, type, lexigram):
        self.type = type
        self.lexigram = lexigram
 
    def get_string(self):
        return "Token[type: " + self.type + ", lexigram: " + self.lexigram + "]"

def scan(query):
    tokens = []
    for token in query:
        if token.isnumeric():
            aux = Token('NUM',token)
            tokens.append(aux)
        elif token == '+':
            aux = Token('PLUS',token)
            tokens.append(aux)
        elif token == '-':
            aux = Token('MINUS',token)
            tokens.append(aux)
        elif token == '/':
            aux = Token('SLASH',token)
            tokens.append(aux)
        elif token == '*':
            aux = Token('STAR',token)
            tokens.append(aux)
        else:
            raise ValueError("Operador desconhecido: " + token)
    return tokens


def calculate(tokens):
    stack = []

    for token in tokens:
        if token.type == 'NUM':
            stack.append(float(token.lexigram))
        elif token.type == 'PLUS':
            try:
                aux = stack.pop()
                aux = stack.pop() + aux
                stack.append(aux)
            except IndexError:
                raise IndexError("Expressão invalida")
        elif token.type == 'MINUS':
            try:
                aux = stack.pop()
                aux = stack.pop() - aux
                stack.append(aux)
            except IndexError:
                raise IndexError("Expressão invalida")
        elif token.type == 'SLASH':
            try:
                aux = stack.pop()
                aux = stack.pop() / aux
                stack.append(aux)
            except IndexError:
                raise IndexError("Expressão invalida")
        elif token.type == 'STAR':
            try:
                aux = stack.pop()
                aux = stack.pop() * aux
                stack.append(aux)
            except IndexError:
                raise IndexError("Expressão invalida")
        else:
            raise ValueError("Operador desconhecido: " + token)

    if len(stack) == 1:
        return stack.pop()
    else:
        raise ValueError("Expressão invalida")
    

with open("Calc1.stk",'r')as f:
    line = f.read()
    query = line.split("\n")

tokens = scan(query)

result = calculate(tokens)

print(result)
print("///////////////////////////////")
for token in tokens:
    print(token.get_string())