# A\* Search Algorithm for Puzzle 8

This project implements various search algorithms for solving the Puzzle 8 problem. It includes utilities for handling search algorithms, heuristics, and puzzle state management.

## Overview

The goal of this project is to solve the Puzzle 8 problem using different search strategies, including **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, **Uniform Cost Search (UCS)**, **Greedy Search**, and **A\* Search**.

### Puzzle 8

The Puzzle 8 consists of a 3x3 grid with 8 numbered tiles (1-8) and one empty space. The tiles can be moved to the empty space, and the goal is to arrange the tiles in numerical order using the least number of moves.

### Algorithms Implemented

1. **Breadth-First Search (BFS)**

   - Explores all nodes at the current depth before moving to the next level. Guarantees the shortest path (in moves) but is memory-intensive.

2. **Depth-First Search (DFS)**

   - Explores as far as possible along each branch before backtracking. Not optimal (may find a longer path) but uses less memory than BFS.

3. **Uniform Cost Search (UCS)**

   - Finds the least-cost path to the goal without using any heuristic. Guarantees the optimal solution if the cost function is non-negative.

4. **Greedy Search**

   - Uses a heuristic to estimate the distance to the goal and expands the node with the least estimated cost. May not find the optimal solution but is often faster than UCS.

5. **A\* Search**
   - Combines UCS and Greedy Search. Uses both the cost to reach a node and a heuristic to estimate the distance to the goal. Guarantees the optimal solution if the heuristic is admissible.

### Heuristics Implemented

- **h1**: Misplaced tiles heuristic. The cost is the number of tiles not in their goal position.
- **h2**: Manhattan distance heuristic. The cost is the sum of the absolute differences between the current and goal positions for each tile.

## Usage

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/yourusername/puzzle8-search.git
cd puzzle8-search
```

## Running the Puzzle Solver

To run the solver with different algorithms, use the following commands:

```# A* Search (default: Manhattan distance heuristic)
python astar.py

# Uniform Cost Search (UCS)
python ucs.py

# Breadth-First Search (BFS)
python bfs.py

# Depth-First Search (DFS)
python dfs.py
```

## Changing Heuristics

You can change the heuristic used in A\* by passing either `h1` or `h2` to the astar function in the `main()` function

```# Choose heuristic h1 or h2
result = astar(
    initial_state=puzzle.initial_state,
    get_actions=puzzle.get_actions,
    get_state=puzzle.apply_action,
    is_goal=puzzle.is_goal,
    heuristic=h1  # or h2 depending on your choice
)
```

## Folder Structure

```puzzle8-search/
│
├── astar.py                # A* Search algorithm
├── ucs.py                  # UCS algorithm
├── greedy.py               # Greedy Search algorithm
├── puzzle8_game.py         # Puzzle 8 game logic
├── utilities.py            # Helper functions (get_min, compute_cost)
└── README.md               # This file
```
