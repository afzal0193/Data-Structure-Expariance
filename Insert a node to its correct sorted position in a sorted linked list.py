
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node =self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def sortedInsert(self,data):
        if self.head is None or self.head.data>=data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return self.head

        current_node = self.head
        new_node = Node(data)
        while current_node.next is not None and current_node.next.data<new_node.data:
            current_node = current_node.next
        new_node.next =current_node.next
        current_node.next = new_node


if __name__ =="__main__":
    ll = Linklist()
    ll.head = None
    n =int(input())
    for i in range(n):
        val =int(input())
        ll.sortedInsert(val)

    ll.print_list()