### ())))(())   balanced or not ..
"""
def balanced(input_string):
    items = []
    for ch in input_string:
        if ch =="(":
            items.append("(")
        if ch ==")":
            if not items:
                return False

            items.pop()

    return not items

if __name__ =="__main__":
    input_string = input()
    if balanced(input_string):
        print("yes")
    else:
        print("NO")

"""


### same code for chack balanced or not

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False


s = Stack()

input_string = input()


def balanced(input_string):
    for ch in input_string:
        if ch == "(":
            s.push("(")

        if ch == ")":
            if s.is_empty():
                return False
            s.pop()

    return not s.is_empty()


if __name__ == "__main__":
    input_string = input()
    if balanced(input_string):
        print("Yes")
    else:
        print("No")

