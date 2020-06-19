grah = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}

def dfs(grah, start):
    stack = []
    stack.append(start)
    seen = set()
    seen.add(start)
    while len(stack) != 0:
        node = stack.pop()
        nodes = grah[node]
        for item in nodes:
            if item not in seen:
                stack.append(item)
                seen.add(item)
        print(node)

dfs(grah, 'b')