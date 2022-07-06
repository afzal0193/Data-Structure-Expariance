
def balaced(input_string):
    stack = []
    for ch in input_string:

        if ch == "(" or ch =="{" or ch =="[":
            stack.append(ch)

        if not stack and ch in ["}","]",")"]:
            return False
        if ch == ")" and stack[-1] == "(":
            if not stack:
                return False
            stack.pop()

        if ch == "}" and stack[-1] == "{":
            if not stack:
                return False
            stack.pop()

        if ch == "]" and stack[-1] == "[":
            if not stack:
                return False
            stack.pop()
    return  not stack

if __name__ =="__main__":

    input_string =input()
    if balaced(input_string):
        print("Yes")
    else:
        print("No")
