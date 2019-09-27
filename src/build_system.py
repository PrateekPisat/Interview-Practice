import random

def build_system(package_deps):
    graph = dict()
    v_set = set()
    t_order = list()

    for package, deps in package_deps:
        graph[package] = deps

    nodes = set(graph.keys())

    while nodes != v_set:
        root = random.choice(list(nodes - v_set))
        explore_subtree(root, t_order, v_set, graph)

    return t_order


def explore_subtree(root, t_order, v_set, graph):
    if not root:
        return t_order
    v_set.add(root)
    for child in graph[root]:
        if child not in v_set:
            t_order = explore_subtree(child, t_order, v_set, graph)

    t_order.append(root)
    return t_order
