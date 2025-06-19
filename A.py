from pprint import pprint
from queue import PriorityQueue

# Graph and heuristic definitions
G = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Dharan": 20, "Biratchowk": 30},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Itahari": 30, "Kanepokhari": 10,"Biratnagar":30},
    "Kanepokhari": {"Biratchowk": 10, "Urlabari": 12, "Rangeli": 25},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25,"Urlabari":40},
    "Urlabari": {"Kanepokhari": 12, "Damak": 6,"Rangeli":40},
    "Damak": {"Urlabari": 6}
}

h = {
    'Biratnagar': 46,
    'Itahari': 39,
    'Dharan': 41,
    'Rangeli': 28,
    'Biratchowk': 29,
    'Kanepokhari': 17,
    'Urlabari': 6,
    'Damak': 0,
}

# A* Algorithm
def aStar(G, h, start, goal):
    # Initialize a Priority Queue, prev dict, visited set
    PQ = PriorityQueue()
    prev = dict()
    visited = set()
    
    # Enqueue the start state with its f-score (g+h)
    PQ.put((h[start], (start, 0)))
    prev[start] = ""  # The start node has no previous node (empty string)
    
    # Repeat until the Priority Queue is empty
    while not PQ.empty():
        # Dequeue the node with the lowest f-score
        outStateForce, (outstate, outstateGScore) = PQ.get()
        
        # If the current state is the goal state, return success
        if outstate == goal:
            return True, prev, outstateGScore
        
        # Mark the current state as visited
        visited.add(outstate)
        
        # Iterate over the neighbors
        for chimeki in G[outstate]:
            if chimeki not in visited:
                chimekiGScore = outstateGScore + G[outstate][chimeki]
                PQ.put((chimekiGScore + h[chimeki], (chimeki, chimekiGScore)))   
                prev[chimeki] = outstate
    
    # If the goal is not found, return failure
    return False, prev, -1

# Path reconstruction function
def reconstruct_path(previous, goal):
    path = goal
    while previous[goal] != "":
        path = previous[goal] + " -> " + path
        goal = previous[goal]
    return path

# Start and goal
start = "Biratnagar"
goal = "Damak"

# Execute A* search
goalFound, previous, cost = aStar(G, h, start, goal)

# Output the results
if goalFound:
    print("Path:", reconstruct_path(previous, goal))
    print("Total cost:", cost)
else:
    print("No Solution!")
     
