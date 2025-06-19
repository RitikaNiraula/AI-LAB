from queue import PriorityQueue

def astar(start, goal):
    def puzzle(state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def get_chimekis(state):
        chimekis = []
        x, y = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                chimekis.append(tuple(tuple(row) for row in new_state))
        return chimekis

    pq = PriorityQueue()
    pq.put((0 + puzzle(start), 0, start, [])) 
    visited = set()

    while not pq.empty():
        _,cost, current, path = pq.get()

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [current]

        for chimeki in get_chimekis(current):
            if chimeki not in visited:
                f_cost = cost + 1 + puzzle(chimeki)
                pq.put((f_cost, cost + 1, chimeki, path + [current]))

    return None


start_state = ((1, 2, 3), (4, 0, 6), (7, 5, 8)) 
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

solution = astar(start_state, goal_state)
if solution:
    print("Solution found!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists.")
