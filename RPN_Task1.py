with open("Calc1.stk",'r')as f:
    line = f.read()
    query = line.split("\n")

stack = []

for token in query:
    if token == '+':
        aux = stack.pop()
        aux = stack.pop() + aux
        stack.append(aux)
    elif token == '-':
        aux = stack.pop()
        aux = stack.pop() - aux
        stack.append(aux)
    elif token == '/':
        aux = stack.pop()
        aux = stack.pop() / aux
        stack.append(aux)
    elif token == '*':
        aux = stack.pop()
        aux = stack.pop() * aux
        stack.append(aux)
    else:
        stack.append(float(token))

print(stack.pop())