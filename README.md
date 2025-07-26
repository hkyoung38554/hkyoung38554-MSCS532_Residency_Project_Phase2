# Pareto-Optimal Multi‑Criteria Pathfinding PoC

This repository contains a proof‑of‑concept implementation of core data structures for Pareto‑optimal, multi‑criteria pathfinding in Python. It demonstrates how to represent a sparse road network, maintain Pareto‑front cost labels, and prioritize label expansion in a lexicographic min‑heap.

## Repository Structure

- **pathfinder/**
  - `graph.py` — Directed adjacency‑list graph with 3‑tuple edge costs.
  - `label.py` — `Label` class encapsulating cost vectors and dominance logic.
  - `label_set.py` — `LabelSet` managing non‑dominated labels per node.
  - `priority_queue.py` — `LabelPriorityQueue` wrapper around `heapq` using lexicographic ordering.

- **tests/**
  - `test_graph.py`, `test_label.py`, `test_label_set.py`, `test_priority_queue.py` — pytest modules with detailed logging.
  - `test_results.txt` — Captured output from `pytest -s --maxfail=1 -q > tests/test_results.txt`.

- **demo.py**
  Standalone script demonstrating core operations and a combined Pareto‑expansion loop. Outputs written to `demo_results.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Oishani/MSCS_532_Project.git
   cd MSCS_532_Project
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```

## Usage

- **Run Unit Tests**
  ```bash
  python3 -m pytest -s --maxfail=1 -q > tests/test_results.txt
  ```

- **Run Demo Script**
  ```bash
  python3 demo.py
  # → Outputs captured in demo_results.txt
  ```

## Next Steps

- Implement the unified label‑expansion driver and path‑reconstruction logic.
- Abstract dominance and ordering policies for user‑defined criteria.
- Integrate with real map data and a user interface for end‑to‑end pathfinding.