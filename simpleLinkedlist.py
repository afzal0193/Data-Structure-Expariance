
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node =self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


if __name__ =="__main__":
    frist = Node(1)
    secound =Node(2)
    third = Node(3)
    foruth = Node(4)
    head = frist
    frist.next = secound
    secound.next = third
    third.next = foruth
    foruth.next = None
    ll = linkedlist()
    ll.head = frist
    ll.print_list()


