import heapq          
import time


MAP_A = [
    "S..#....",
    "##.#.##.",
    "....~~..",
    ".####.#.",
    "...~..#G",
]

MAP_B = [
    "S~~~~~~~G",
    ".#######.",
    ".........",
    ".#.#.#.#.",
    ".........",
]

MAP_C = [
    "S..#....",
    ".#.#.##.",
    "...#..#.",
    ".###.##.",
    "....#..G",
]

GRID = MAP_A   # to switch the maps

# Cost of ENTERING a cell
COSTS = {".": 1, "~": 3, "S": 1, "G": 1}


def find_symbol(grid, symbol):
    for r, row in enumerate(grid):
        if symbol in row:
            return (r, row.index(symbol))
    return None

def get_neighbors(grid, pos):
    """Return the possible cells to move to"""
    r, c = pos
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   # up, down, left, right
        nr, nc = r + dr, c + dc
        inside = 0 <= nr < len(grid) and 0 <= nc < len(grid[0])
        if inside and grid[nr][nc] != "#":
            result.append(((nr, nc), COSTS[grid[nr][nc]]))
    return result


def reconstruct_path(parent, goal):
    """Walk back from goal to start."""
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def UCS(grid):
    start = find_symbol(grid, 'S')
    goal = find_symbol(grid, "G")

    # Priority queue stores: (accumulated_cost, current_position)
    priority_queue = [(0, start)]
    parent = {start: None}
    g_costs = {start: 0}
    explored_count = 0

    done = set()
    max_frontier = 1 #maximum number of nodes waiting in the priority queue

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in done:
            continue
        done.add(current_node)
        
        if current_node == goal:
            return current_cost, reconstruct_path(parent, goal), explored_count, max_frontier
        
        explored_count += 1

        for neighbor, move_cost in get_neighbors(grid, current_node):
            new_cost = current_cost + move_cost

            is_new_node = neighbor not in g_costs
            is_cheaper_path = not is_new_node and new_cost < g_costs[neighbor]

            if is_new_node or is_cheaper_path:
                g_costs[neighbor] = new_cost        
                parent[neighbor] = current_node     
                heapq.heappush(priority_queue, (new_cost, neighbor))
        
        max_frontier = max(max_frontier, len(priority_queue))

    return  None, [], explored_count, max_frontier


# A* Algorithm

def manhattan(a, b):
    """Our guess: how many rows + columns away is this cell from G."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid):
    start = find_symbol(grid, "S")
    goal = find_symbol(grid, "G")

    # queue stores (f, position), f = cost so far + guess to goal
    queue = [(manhattan(start, goal), start)]
    parent = {start: None}
    g_costs = {start: 0}
    done = set()
    explored_count = 0
    max_frontier = 1

    while queue:
        f, current = heapq.heappop(queue)

        # we may push the same cell more than once, skip the old copies
        if current in done:
            continue
        done.add(current)

        if current == goal:
            return g_costs[goal], reconstruct_path(parent, goal), explored_count, max_frontier

        explored_count += 1

        for neighbor, move_cost in get_neighbors(grid, current):
            new_g = g_costs[current] + move_cost

            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                parent[neighbor] = current
                f_new = new_g + manhattan(neighbor, goal)
                heapq.heappush(queue, (f_new, neighbor))

        max_frontier = max(max_frontier, len(queue))

    # nothing left to explore and we never got to G
    return None, [], explored_count, max_frontier


# quick test of A* on the 3 maps
if __name__ == "__main__":
    for name, grid in [("MAP_A", MAP_A), ("MAP_B", MAP_B), ("MAP_C", MAP_C)]:
        start_time = time.perf_counter()
        cost, path, explored, max_f = astar(grid)
        ms = (time.perf_counter() - start_time) * 1000

        print("A* on", name)
        if path:
            print("path:", path)
            print("length:", len(path), "| cost:", cost)
        else:
            print("No path found")
        print("expanded:", explored, "| max frontier:", max_f, "| time: %.3f ms" % ms)
        print()
