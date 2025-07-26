from typing import Any, Tuple, Optional

class Label:
    """Multi-dimensional cost label for Pareto paths."""
    def __init__(self, cost: Tuple[float, float, float], node: Any, predecessor: Optional['Label'] = None):
        if not (isinstance(cost, tuple) and len(cost) == 3):
            raise ValueError("Cost must be a 3-tuple")
        self.cost = cost
        self.node = node
        self.predecessor = predecessor

    def dominates(self, other: 'Label') -> bool:
        """Return True if self <= other in all dims and < in at least one."""
        return all(a <= b for a, b in zip(self.cost, other.cost)) and any(a < b for a, b in zip(self.cost, other.cost))

    def __lt__(self, other: 'Label') -> bool:
        """Lexicographic ordering: time, toll, scenic."""
        return self.cost < other.cost

    def __repr__(self) -> str:
        return f"Label(node={self.node}, cost={self.cost})"