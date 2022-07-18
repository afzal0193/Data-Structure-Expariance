
class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        if not self.items:
            return True
        return False

    def pop(self):
        return self.items.pop()

    def append(self,data):
        self.items. append(data)

    def main_func(self,input_string):
        for ch in input_string:
            if ch =="(":
                self.append("(")
            elif ch ==')':
                if self.is_empty():
                    return False

                self.items.pop()
        return not self.items
if __name__ =="__main__":
    obj = stack()
    if obj.main_func(input()):
        print("yes")
    else:
        print("no")





