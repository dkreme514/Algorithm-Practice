

def node2list(node):
    output = []
    while node:
        output.append(node.data)
        node = node.next
    return output
class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
#class SinglyLinkedList:
    def __init__(self):
        self.head = None
def oddEvenList(l):
    if not l or not l.next:
        return l
    odd = l
    even = even_h = l.next
    while odd.next and even.next:
        odd.next = even.next
        if odd.next:
            even.next =odd.next.next
        odd = odd.next
        even = even.next
    odd.next = even_h
    return l

list1 = SinglyLinkedList()