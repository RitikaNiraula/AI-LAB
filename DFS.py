import pprint

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

def DFS(G,start,goal):
    # initialize a stack
    stack=list()
    # initialize a dictionary to reconstruct a path
    prev=dict()
    # initialize a set to keep track of visited vertices
    visited=set()
    # Push the starting state into the stack
    stack.append(start)
    # Push the starting state of startin state to " "
    prev[start]=" "
    # Repeat until the stack is not empty
    while(stack):
        # pop a state from the stack
        poppedState=stack.pop()
        # Mark the state as visited
        visited.add(poppedState)
        # Return if the poppedState is the goal
        if poppedState==goal:
            return True,prev
            # Pushed all the chimekis of Poppedstate if they are not already in the stack
            # and if they are not already visited
        for chimeki in G[poppedState]:
            if chimeki not in stack and chimeki not in visited:
                stack.append(chimeki)
                prev[chimeki]=poppedState
    return False,prev  


def reconstruct_path(G,previous,goal):
    path=goal
    while (previous[goal]!=' '):
        path=previous[goal]+'->'+path
        goal=previous[goal]
    return path

def computeCost(solutionPath):
     pathList=solutionPath.split('->')

start="Biratnagar"  
goal="Damak"   
goalFound,previous=DFS(G,start,goal)
if(goalFound):
    print(reconstruct_path(G,previous,goal))
else:
    print("No Solution!")       