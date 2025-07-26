from collections import deque
from typing import Any, Dict, List, Tuple

class Graph:
    """Directed graph with adjacency list and multi-dimensional edge weights."""
    def __init__(self):
        self._adj: Dict[Any, List[Tuple[Any, Tuple[float, float, float]]]] = {}

    def add_node(self, node: Any) -> None:
        """Add a node to the graph."""
        if node not in self._adj:
            self._adj[node] = []

    def add_edge(self, u: Any, v: Any, cost: Tuple[float, float, float]) -> None:
        """Add a directed edge u -> v with a cost vector."""
        if not (isinstance(cost, tuple) and len(cost) == 3):
            raise ValueError("Cost must be a tuple of three floats")
        self.add_node(u)
        self.add_node(v)
        self._adj[u].append((v, cost))

    def remove_node(self, node: Any) -> None:
        """Remove a node and all edges to/from it."""
        if node not in self._adj:
            raise KeyError(f"Node {node} not found")
        del self._adj[node]
        for nbrs in self._adj.values():
            nbrs[:] = [(n, c) for n, c in nbrs if n != node]

    def remove_edge(self, u: Any, v: Any) -> None:
        """Remove directed edge u -> v."""
        if u not in self._adj:
            raise KeyError(f"Node {u} not found")
        before = len(self._adj[u])
        self._adj[u] = [(n, c) for n, c in self._adj[u] if n != v]
        if len(self._adj[u]) == before:
            raise ValueError(f"Edge {u} -> {v} not found")

    def neighbors(self, node: Any) -> List[Tuple[Any, Tuple[float, float, float]]]:
        """Return neighbors and costs for node."""
        if node not in self._adj:
            raise KeyError(f"Node {node} not found")
        return list(self._adj[node])

    def bfs(self, start: Any) -> List[Any]:
        """Breadth-first traversal from start node. Returns list of visited nodes."""
        if start not in self._adj:
            raise KeyError(f"Node {start} not found")
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v, _ in self._adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return order

    def dfs(self, start: Any) -> List[Any]:
        """Depth-first traversal from start node. Returns list of visited nodes."""
        if start not in self._adj:
            raise KeyError(f"Node {start} not found")
        visited = set()
        order = []
        def _dfs(u: Any):
            visited.add(u)
            order.append(u)
            for v, _ in self._adj[u]:
                if v not in visited:
                    _dfs(v)
        _dfs(start)
        return order