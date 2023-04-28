import re 

class Token:
    def __init__(self, type, lexigram):
        self.type = type
        self.lexigram = lexigram
 
    def get_string(self):
        return "Token[type: " + self.type + ", lexigram: " + self.lexigram + "]"

def scan(query):
    tokens = []

    # Números com virgula \d+\.\d
    # Números \d+
    # Operadores [+*/-]

    for token in query:
        if re.match(r'(\d+\.\d+|\d+)', token):
            aux = Token('NUMBER',token)
            tokens.append(aux)
        elif re.match(r'[+*/-]', token):
            aux = Token('OPERATOR',token)
            tokens.append(aux)
        else:
            raise ValueError("Caracter desconhecido: " + token)
    return tokens


def calculate(tokens):
    stack = []

    for token in tokens:
        if token.type == 'NUMBER':
            stack.append(float(token.lexigram))
        elif token.type == 'OPERATOR':
            if token.lexigram == '+':
                try:
                    aux = stack.pop()
                    aux = stack.pop() + aux
                    stack.append(aux)
                except IndexError:
                    raise IndexError("Expressão invalida")
            elif token.lexigram == '-':
                try:
                    aux = stack.pop()
                    aux = stack.pop() - aux
                    stack.append(aux)
                except IndexError:
                    raise IndexError("Expressão invalida")
            elif token.lexigram == '/':
                try:
                    aux = stack.pop()
                    aux = stack.pop() / aux
                    stack.append(aux)
                except IndexError:
                    raise IndexError("Expressão invalida")
            elif token.lexigram == '*':
                try:
                    aux = stack.pop()
                    aux = stack.pop() * aux
                    stack.append(aux)
                except IndexError:
                    raise IndexError("Expressão invalida")
        else:
            raise ValueError("Caracter desconhecido: " + token)

    if len(stack) == 1:
        return stack.pop()
    else:
        raise ValueError("Expressão invalida")
    

with open("Calc1.stk",'r')as f:
    line = f.read()
    query = line.split("\n")

tokens = scan(query)

result = calculate(tokens)

barrinhas = 15

print("Resultado: " + str(result))
print("/" * barrinhas + " Tokens " + "/" * barrinhas)
for token in tokens:
    print(token.get_string())