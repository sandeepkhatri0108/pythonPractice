parensIterator = iter('(){}[]<>')
parensMapval = dict(zip(parensIterator, parensIterator))
parensclosing = parensMapval.values()
print ("Enter value as balanced(String)")
def balanced(inputStr):
    stack = []
    for char in inputStr:
        data = parensMapval.get(char, None)
        if data:
            stack.append(data)
        elif char in parensclosing:
            if not stack or char != stack.pop():
                return False
    return not stack