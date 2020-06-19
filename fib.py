def cache(func):
    data = {}
    def wrapper(n):
        if n in data:
            return data[n]
        else:
            res = func(n)
            data[n] = res
            return res
    return wrapper

@cache  # fib = cache(fib )
def fib(n):
    if n <= 2:
        return 1
    else:

        
        return fib(n-1) + fib(n-2)
for i in range(1, 35):
    print(fib(i))

class Node(object):
    def __init__(self, pre = None, next = None, key = None, value = None):
        self.pre, self.next, self.key, self.value = pre, next, key, value

class CircularDoubleLinkedList(object):
    def __init__(self):
        node = Node()
        node.pre, node.next = node, node
        self.rootnode = node
    def headnode(self)::
        return self.rootnode.next
    def tailnode(self):
        return self.rootnode.pre
    def remove(self, node):
        if node is self.rootnode:
            return
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
    def append(self, node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.next = self.rootnode
        self.rootnode.pre = node 