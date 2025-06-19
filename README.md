# AI-LAB2
A* theory refers to the underlying principles of the A* (A-star) algorithm, a widely used pathfinding and graph traversal technique in computer science and artificial intelligence. A* is designed to efficiently find the shortest path between two points by combining features of Dijkstra's algorithm and a greedy best-first search. 
It uses a cost function f(n)=g(n)+h(n), where g(n) is the exact cost from the starting node to node h(n) is a heuristic that estimates the cost from n to the goal. 
The heuristic function must be admissible, meaning it never overestimates the true cost to reach the goal, to guarantee optimality. A* theory emphasizes how the choice of the heuristic affects the algorithm’s performance and accuracy. A well-designed heuristic can significantly reduce the number of explored nodes, making A* both optimal and efficient for many real-world applications such as robotics, navigation systems, and game development.


Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It starts at a selected node (often called the source or root) and explores each adjacent node one by one, going deeper into the graph until it reaches a node with no unvisited adjacent nodes. Then it backtracks to explore other branches. DFS can be implemented using recursion or with an explicit stack. 
It is commonly used to detect cycles in graphs, solve puzzles, and analyze connectivity. DFS works on both directed and undirected graphs, and while it does not always find the shortest path, it is efficient in space and time when used with appropriate conditions.


