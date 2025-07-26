"""
Demonstration script for core pathfinding data structures.
"""

from pathfinder.graph import Graph
from pathfinder.label import Label
from pathfinder.label_set import LabelSet
from pathfinder.priority_queue import LabelPriorityQueue
from contextlib import redirect_stdout


def demo_graph():
    print("=== Graph Demo ===")
    g = Graph()
    # Add nodes and edges
    for node in ['A', 'B', 'C', 'D']:
        g.add_node(node)
    g.add_edge('A', 'B', (1, 1, 1))
    g.add_edge('A', 'C', (2, 0, 1))
    g.add_edge('B', 'D', (0, 3, 2))
    g.add_edge('C', 'D', (1, 1, 0))
    # Show adjacency
    print("Adjacency List:", g._adj)
    print("Neighbors of A:", g.neighbors('A'))
    # Traversals
    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))
    # Error handling demo
    try:
        g.remove_edge('A', 'D')
    except Exception as e:
        print("Expected error removing non-existent edge:", e)
    print()


def demo_label_set():
    print("=== LabelSet Demo ===")
    ls = LabelSet()
    labels = [Label((5, 5, 5), 'X'),
              Label((3, 7, 5), 'X'),
              Label((5, 4, 6), 'X'),
              Label((5, 5, 5), 'X')]
    for lbl in labels:
        added = ls.add(lbl)
        status = 'Added' if added else 'Dominated'
        print(f"Adding {lbl}: {status}; Current set = {ls.labels}")
    print()


def demo_priority_queue():
    print("=== LabelPriorityQueue Demo ===")
    pq = LabelPriorityQueue()
    labels = [Label((5, 1, 1), 'A'),
              Label((3, 2, 2), 'B'),
              Label((3, 1, 3), 'C')]
    for lbl in labels:
        print(f"Pushing {lbl}")
        pq.push(lbl)
    print("Queue content before pops:", pq)
    while pq:
        lbl = pq.pop()
        print("Popped:", lbl)
    # Pop empty queue
    try:
        pq.pop()
    except Exception as e:
        print("Expected error popping empty queue:", e)
    print()


def demo_combined():
    print("=== Combined Demo: Simple Pareto Expansion ===")
    # Build a small graph
    g = Graph()
    g.add_edge('S', 'A', (1, 2, 3))
    g.add_edge('S', 'B', (2, 1, 3))
    g.add_edge('A', 'T', (1, 1, 1))
    g.add_edge('B', 'T', (1, 1, 2))
    
    # Initialize label sets and PQ
    nodes = ['S', 'A', 'B', 'T']
    label_sets = {n: LabelSet() for n in nodes}
    pq = LabelPriorityQueue()
    start = Label((0, 0, 0), 'S')
    label_sets['S'].add(start)
    pq.push(start)

    # Expand labels
    while pq:
        lbl = pq.pop()
        print("Expanding", lbl)
        for nbr, cost in g.neighbors(lbl.node):
            new_cost = tuple(x + y for x, y in zip(lbl.cost, cost))
            new_lbl = Label(new_cost, nbr, lbl)
            if label_sets[nbr].add(new_lbl):
                pq.push(new_lbl)
                print(f"  -> New non-dominated label at {nbr}: {new_lbl}")

    # Show results
    print("Final label sets:")
    for node, ls in label_sets.items():
        print(f"  {node}: {ls.labels}")
    print()


if __name__ == '__main__':
    # Redirect all demo output to demo_results.txt
    with open('demo_results.txt', 'w') as f:
        with redirect_stdout(f):
            demo_graph()
            demo_label_set()
            demo_priority_queue()
            demo_combined()
    print("Demo results written to demo_results.txt")
