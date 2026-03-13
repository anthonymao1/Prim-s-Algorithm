import heapq

def prim(graph, start):
    visited = set([start])
    edges = []
    heap = []

    for to, weight in graph[start]:
        heapq.heappush(heap, (weight, start, to))

    while heap:
        weight, frm, to = heapq.heappop(heap)
        if to not in visited:
            visited.add(to)
            edges.append((frm, to, weight))

            for nxt, w in graph[to]:
                if nxt not in visited:
                    heapq.heappush(heap, (w, to, nxt))

    return edges

if __name__ == "__main__":
    graph = {
        "A":[("B",1),("C",3)],
        "B":[("A",1),("C",1),("D",4)],
        "C":[("A",3),("B",1),("D",1)],
        "D":[("B",4),("C",1)]
    }

    print("Prim MST:", prim(graph,"A"))
