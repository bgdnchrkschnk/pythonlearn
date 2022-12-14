import os
def checkio(expression):
    stack = []
    pairs = {"(" : ")", "{" : "}", "[" : "]"}
    for symbol in expression:
        if symbol in pairs.keys():
            stack.append(symbol)
        elif symbol in pairs.values():
            if len(stack) == 0:
                return False
            else:
                if pairs[stack[-1]] == symbol:
                    stack.pop()
                else:
                    return False
    return bool(len(stack))

