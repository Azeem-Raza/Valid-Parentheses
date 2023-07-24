def ValidParentheses(s):
    stack = [] #created a variable where the character will be stored
    open = "({["
    close = ")}]"

    for char in s: #iterate through each character in string.
        if char in open:
            stack.append(char)
        elif char in close:
            if not stack:
                return False
            if open.index(stack.pop()) != close.index(char):
                return False
    return len(stack) == 0

parentheses = input("Enter a string of parentheses: ")
if ValidParentheses(parentheses):
    print("Valid parentheses")
else:
    print("Invalid parentheses")