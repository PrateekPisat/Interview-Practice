import math

def lies_on_path(source, end, graph):
    v_parent = dict()
    v_dist = dict()
    heap_map = dict()
    neighbours = dict()
    edges = dict()

    # Init
    for src, dest, cost in graph:
        heap_map[src] = math.inf
        heap_map[dest] = math.inf
        neighbours[src] = neighbours.get(src, list()) + [dest]
        neighbours[dest] = neighbours.get(dest, list()) + [src]
        edges[src] = edges.get(src, dict())
        edges[src][dest] = cost
        edges[dest] = edges.get(dest, dict())
        edges[dest][src] = cost
    v_dist[source] = 0
    v_parent[source] = [None]

    while heap_map:
        for dest in neighbours[source]:
            if dest in heap_map.keys() and v_dist[source] + edges[source][dest] == heap_map[dest]:
                heap_map[dest] = v_dist[source] + edges[source][dest]
                v_dist[dest] = v_dist[source] + edges[source][dest]
                v_parent[dest] = v_parent[dest] + [source]
            if dest in heap_map.keys() and v_dist[source] + edges[source][dest] < heap_map[dest]:
                heap_map[dest] = v_dist[source] + edges[source][dest]
                v_dist[dest] = v_dist[source] + edges[source][dest]
                v_parent[dest] = [source]

        del(heap_map[source])
        if heap_map:
            source = min(heap_map, key=heap_map.get)

    # Path to Dest
    paths_to_dest = build_paths(v_parent, end, list(), list())
    edge_paths = build_edge_paths(paths_to_dest)

    result = list()
    for src, dest, cost in graph:
        result.append(True) if tuple([src, dest]) in edge_paths else result.append(False)
    return result


def build_paths(v_parent, dest, current_path, paths):
    if not dest:
        paths.append(tuple(current_path[::-1]))
        return paths
    for par in v_parent[dest]:
        paths = build_paths(v_parent, par, current_path + [dest], paths)
    return paths


def build_edge_paths(paths):
    edge_paths = set()
    for path in paths:
        for i in range(0, len(path) - 1):
            edge_paths.add(tuple([path[i], path[i+1]]))
            edge_paths.add(tuple([path[i+1], path[i]]))
    return edge_paths
