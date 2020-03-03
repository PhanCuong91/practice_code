class Node(object):
    def __init__(self, value=None):
        self.element = value
        self.nextNode = None


class LinkedList():
    def __init__(self):
        self.head = None


l = LinkedList()
e1 = Node('1')
e2 = Node('2')
e3 = Node('3')
e4 = Node('4')
l.head = e1
e1.nextNode = e2
e2.nextNode = e3
e3.nextNode = e4


def check_cycle(node):
    marker_1 = node
    marker_2 = node
    while marker_2 != None and marker_2.nextNode != None:
        marker_1 = marker_1.nextNode
        marker_2 = marker_2.nextNode.nextNode
        if marker_1 == marker_2:
            return True
    return False


def reserve(node):
    while node.nextNode != None:
        curNode = node
        while curNode.nextNode != None:
                preNode = curNode
                curNode = curNode.nextNode
        preNode.nextNode = None
        print(curNode.element)
    print(node.element)


def nth_to_last_node(node, n):
    curNode = node
    arr = []
    while curNode.nextNode != None:
        arr.append(curNode.element)
        curNode = curNode.nextNode
        print(arr)
    arr.append(curNode.element)
    if (len(arr) <= n):
        return False
    return arr[len(arr)-n-1]


#(reserve(e1))
print(nth_to_last_node(e1, 3))
print(check_cycle(e1))