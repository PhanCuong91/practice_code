""""
Problem:
Given a string of opening and closing parentheses, check whether it is balanced. we have 3 types of parentheses:
round bracket(), square bracket [] and curly bracket {}. Assume that the string does not contain any other character
than these, no spaces, words or numbers.
"""


import stack_queue


def balanced_parentheses(s):
    stack = stack_queue.Stack()
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.push(i)
        else:
            if (i == ')' and stack.pop() != '(') \
                    or (i == ']' and stack.pop() != '[') \
                    or (i == '}' and stack.pop() != '{'):
                return False
    return True


def balanced_parentheses_1(s):
    if len(s)%2 != 0:
        return False
    opening = set('([{')
    matches = set([('(', ')'), ('{', '}'), ('[', ']')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if (stack.pop(), paren) not in matches:
                return False
    return len(stack) == 0


print(balanced_parentheses_1('(){[()]}'))
print(balanced_parentheses_1('(]{[()]}'))
