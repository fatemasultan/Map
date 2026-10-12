# main.py runs UCS and A* and shows the results
# How to change the map: edit the GRID line below (MAP_A, MAP_B or MAP_C)

import time
from Algorithms import MAP_A, MAP_B, MAP_C, UCS, astar

GRID = MAP_A  

def draw_path(grid, path):
    rows = [list(row) for row in grid]      # turn each string into a list so we can edit it
    for r, c in path:
        if rows[r][c] not in "SG":
            rows[r][c] = "*"
    for row in rows:
        print("".join(row))

def run(algo, grid):
    #Run one algorithm and measure how long it takes
    start = time.perf_counter()
    cost, path, expanded, max_frontier = algo(grid)
    ms = (time.perf_counter() - start) * 1000
    return cost, path, expanded, max_frontier, ms

def show_result(name, grid, result):
    #Print the details of one algorithm on one map
    cost, path, expanded, max_frontier, ms = result
    print("Algorithm:", name)
    if path:
        print("Path:", path)
        print("Total cost:", cost)
        print("Nodes expanded:", expanded)
        draw_path(grid, path)
    else:
        print("No path found")
        print("Nodes expanded:", expanded)
    print()


algorithms=[("UCS", UCS), ("A*", astar)]
all_maps=[("MAP_A", MAP_A), ("MAP_B", MAP_B), ("MAP_C", MAP_C)]

# details for the map chosen in GRID
for name, algo in algorithms:
    show_result(name, GRID, run(algo, GRID))

# results table for all 3 maps
print("Map   | Algorithm | Length | Cost | Expanded | Max frontier | Time (ms)")
print("-" * 70)
for map_name, grid in all_maps:
    for name, algo in algorithms:
        cost, path, expanded, max_frontier, ms = run(algo, grid)
        length = len(path) - 1 if path else "-"     # number of moves
        cost = cost if path else "-"
        print(f"{map_name:<6}| {name:<10}| {length:<7}| {cost:<5}| {expanded:<9}| {max_frontier:<13}| {ms:.3f}")