
## Stack data structure


class Stack:     #stack class
    def __init__(self):   #initilize data storeage ..
        self.items =[]

    def push(self,data):            #push data form this functions
        self.items.append(data)


    def pop(self):                 #pop data from this function
        return self.items.pop()


    def is_empty(self):    #chack stack is empty or not
        if not self.items:
            return True
        else:
            return False

if __name__ =="__main__":   #driver code
    s = Stack()
    s.push(3)
    s.push(33)
    s.push("Afzal")
    s.push("Khan")
    s.push("kdkdk")
    while not s.is_empty():
        print(s.pop())

