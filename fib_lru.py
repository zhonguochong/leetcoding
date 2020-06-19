class Node(object):
    def __init__(self, pre = None, next = None, key = None, value = None):
        self.pre, self.next, self.key, self.value = pre, next, key, value


class CircularDoubleLinkedList(object):
    def __init__(self):
        node = Node()
        node.pre, node.next = node, node
        self.rootnode = node
    
    def headnode(self):
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


class lru_cache(object):
    def __init__(self, maxsize = 15):
        self.maxsize = maxsize
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= self.maxsize
    
    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:
                self.access.remove(cachenode)
                self.access.append(cachenode)
                return cachenode.value
            else:
                value = func(n)
                if self.isfull:
                    headnode = self.access.headnode()
                    del self.cache[headnode.key]
                    self.access.remove(headnode)
                    newnode = Node(self.access.tailnode(), self.access.rootnode, n, value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                else:
                    newnode = Node(self.access.tailnode(), self.access.rootnode, n, value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                    self.isfull = len(self.cache) >= self.maxsize
                return [value, len(self.cache)]
        return wrapper


@lru_cache()  # fib = cache(fib )
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(1, 35):
    print(fib(i))

