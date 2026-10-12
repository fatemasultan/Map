# 1. Project Overview
## This project implements and compares two search algorithms—Uniform Cost Search (UCS) and A*—to find a path from a start cell (S) to a goal cell (G) in a grid.

- **S** — starting position
- **G** — goal position
- **.** — normal cell, with an entry cost of 1
- **~** — water cell, with an entry cost of 3
- **#** — wall/obstacle that cannot be crossed
- **/*** — a cell on the final path, shown by the display function
Movement is allowed only in four directions: up, down, left, and right.

# 2. Algorithms
## Uniform Cost Search (UCS)
UCS always expands the frontier node with the lowest accumulated cost so far.
## A* Search
A* prioritizes nodes using:
f(n) = g(n) + h(n)
Where:
- **g(n)** is the cost from the start to the current cell.
- **h(n)** is the estimated cost from the current cell to the goal.
- **f(n)** is the estimated total cost of a route through that cell.
- 
# Manhattan distance as the heuristic:
## h(n) = abs(current_row - goal_row) + abs(current_column - goal_column)
Manhattan distance counts the minimum number of horizontal and vertical steps to the goal.

# 3. Output Metrics
-**Path**: The sequence of (row, column) coordinates from S to G.
- **Length**: gives the number of moves, not the number of cells. 
- **Total cost**: The sum of the costs of entering cells along the path. 
- **Nodes expanded**: The number of non-goal nodes processed by the algorithm.
- **Max frontier**: The largest number of entries in the priority queue observed during the search.

# 4. Comparing UCS and A*
## Both algorithms seek a minimum-cost route, but they choose which frontier node to process differently:
- UCS uses the accumulated cost g(n).
- A* uses accumulated cost plus estimated remaining cost, g(n) + h(n).
