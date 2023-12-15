def is_balanced(expression): #expression as a string
    stack = []

    brackets_set = {'(': ')', '[': ']', '{': '}'}

    for exp in expression:
        #membership operator, in, to check for a match
        if exp in brackets_set.keys():
            stack.append(exp) #adds key to stack
        elif exp in brackets_set.values():
            if not stack or brackets_set[stack.pop()] != exp:
                return False
            
    return not stack

# test cases
expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1))
print(is_balanced(expression2))