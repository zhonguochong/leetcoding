grah = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}

def bfs(grah, start):
    sequene = []
    sequene.append(start)
    seen = set()
    seen.add(start)
    parent = {start: None}
    while len(sequene) != 0:
        vertex = sequene.pop(0)
        nodes = grah[vertex     ]
        for item in nodes:
            if item not in seen:
                sequene.append(item)
                seen.add(item)
                parent[item] = vertex
        # print(vertex)
    return parent

ps = bfs(grah, 'a')
for key, value in ps.items():
    print(key, value)

# for key in ps:
#     print(key, ps[key])

v = 'd'
while v != None:
    print(v)
    v = ps[v] 