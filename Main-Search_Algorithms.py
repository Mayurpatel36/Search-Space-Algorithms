# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:26:20 2022

@author: Mayur Patel
@Student number: 215481385
@Assingment: MMAI5000 Assignment 1
"""


# Simple node
def get_node(name, weight=0, heuristic = 0):
    node = {}
    node['name'] = name
    node['children'] = []
    node['weight'] = weight
    node['heuristic'] = heuristic
    node['path'] = []

    return node


def add_child(node, name, weight=0, heuristic = 0):
    node['children'].append(get_node(name, weight, heuristic))
 
    
 # The get path function will store the childs, parent each time the child is searched. This will help create
 # the final path. There is also a weight aspect that will create a list with the parent, and the weight that 
 # has been associated with travelling from parent to child. We will later split this up to return the final output
def get_path(child,state):
    # Create a list of the weight of the node to add
    weight = [child['weight']]
    # Set the path taken to include the childs name
    child['path'] = [child['name']]
    # Add the childs name to the path that was taken to get here. i.e. from its parent's path
    path = state['path']
    # Create a list that will store the total path taken to get to this node and the weights for the respective nodes travelled
    child['path'] = path + child['path'] + weight
    return child['path']


# Depth-first search
def DFS(init_state, goal_name):

    frontier = [init_state]
    frontier[0]['path'] = [frontier[0]['name']]
    explored = []
    while len(frontier):
        #Takes the most recently added state to explore using pop(0). This is consistent with LIFO.
        state = frontier.pop(0) # dequeue 
        explored.append(state['name'])
        
        if state['name'] == goal_name:
            
            # This code will split the path taken and the distance travelled
            # into two lists: distance and path
            distance = []
            path = []
            for i in state['path']:
                if type(i) == int:
                    distance.append(i)
                else:
                    path.append(i)
            print ("DFS")
            print ("Path: ", path)
            print ("Total: ", sum(distance))
            return True
        
        # Look at the current states children
        for child in state['children']:
            #If the node has not yet been explored then explore it
            if child['name'] not in explored:
                get_path(child,state)
                # enqueue: insert node at the beginning
                frontier.insert(0, child)
                          
    return False


 # Greedy helper
def find_min_heuristic(frontier):
    # Helper func to find min of h (the heuristic function)
    min_h_i = 0
    
    if len(frontier) > 1:
        min_h = frontier[min_h_i]['heuristic']
        
        for i, state in enumerate(frontier):
 
         
            if state['heuristic'] < min_h:
                min_h_i = i
                min_h = state['heuristic']
             
    return min_h_i
    

def GreedySearch(init_state, goal_name):
    frontier = [init_state]  
    frontier_heuristic = frontier[0]['weight']
    frontier[0]['path'] = [frontier[0]['name']]
    explored = []
    
    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        explored.append(state['name'])
        
        if state['name'] == goal_name:
            # This code will split the path taken and the distance travelled
            # into two lists: distance and path
            
            #By default, include the frontier heuristic in this list as it will always be included in the final paths
            #distance calculation
            distance = [frontier_heuristic]
            path = []
            for i in state['path']:
                if type(i) == int:
                    distance.append(i)
                else:
                    path.append(i)
                    
            print ("Greedy Search")
            print ("Path: ", path)
            print ("Total: ", sum(distance))
            return True
        
        for child in state['children']:
            if child['name'] not in explored:
                get_path(child,state)
                frontier.append(child)
    return False
          


# Breadth-first search
def BFS(init_state, goal_name):

    frontier = [init_state]
    frontier[0]['path'] = [frontier[0]['name']]
    explored = []
    
    while len(frontier):
        state = frontier.pop() # dequeue
        explored.append(state['name'])
   
        if state['name'] == goal_name:
            
            # This code will split the path taken and the distance travelled
            # into two lists: distance and path
            distance = []
            path = []
            for i in state['path']:
                if type(i) == int:
                    distance.append(i)
                else:
                    path.append(i)
            print ("BFS")
            print ("Path: ", path)
            print ("Total: ", sum(distance))
    
            return True

        for child in state['children']:
            if child['name'] not in explored:
                get_path(child,state)
                frontier.insert(0, child)

    return False




# UCS helper
def find_min_weight(frontier):
    # Helper func to find min weight/distance
    min_weight_i = 0
    if len(frontier) > 1:
        min_weight = frontier[min_weight_i]['weight']
        for i, state in enumerate(frontier):
            if state['weight'] < min_weight:
                min_weight_i = i
                min_weight = state['weight']
    return min_weight_i

# Uniform cost search
def UCS(init_state, goal_name):

    frontier = [init_state]
    frontier[0]['path'] = [frontier[0]['name']]
    explored = []
    
    while len(frontier):
        # next state -> state w lowest cost/weight/distance
        state = frontier.pop(find_min_weight(frontier))
        explored.append(state['name'])
        
        
        if state['name'] == goal_name:
            # This code will split the path taken and the distance travelled
            # into two lists: distance and path
            distance = []
            path = []
            
            for i in state['path']:
                if type(i) == int:
                    distance.append(i)
                else:
                    path.append(i)
                    
            print ("UCS")
            print ("Path: ", path)
            print ("Total: ", state['weight'])
            return True
        
        for child in state['children']:
            if child['name'] not in explored:
                child['weight'] += state['weight']
                # Set the path taken to include the childs name
                child['path'] = [child['name']]
                # Add the childs name to the path that was taken to get here. i.e. from its parent's path
                path = state['path']
                # Create a list that will store the total path taken to get to this node and the weights for the respective nodes travelled
                child['path'] = path + child['path'] 
                frontier.append(child)
    return False





# Building the entire search tree based on the assignment for Q1
init_state = 'Kitchener'
goal_name = 'Listowel'

tree = get_node(init_state)

# Children of Kitchener: Guelph, New Hamburg
add_child(tree, 'Guelph', weight=30)
add_child(tree, 'New Hamburg', weight=90)

# Children of Guelph: Drayton
add_child(tree['children'][0], 'Drayton', weight=100)

# Children of Drayton: Listowel
add_child(tree['children'][0]['children'][0], 'Listowel', weight=100)

# Children of New Hamburg: Stratford
add_child(tree['children'][1], 'Stratford', weight=25)

# Children of Stratford: St. Marys, Drayton
add_child(tree['children'][1]['children'][0], 'St. Marys', weight=30)
add_child(tree['children'][1]['children'][0], 'Drayton', weight=200)

# Children of St. Marys: Mitchell
add_child(tree['children'][1]['children'][0]['children'][0], 'Mitchell', weight=80)

# Children of Mitchell: Listowel
add_child(tree['children'][1]['children'][0]['children'][0]['children'][0], 'Listowel', weight=100)

# Children of Drayton: Listowel
add_child(tree['children'][1]['children'][0]['children'][1], 'Listowel', weight=100)




# Building the entire search tree based on the assingment for Q2
init_state = 'Kitchener'
goal_name = 'Listowel'

tree1 = get_node(init_state, heuristic=130)

# Children of Kitchener: Guelph, New Hamburg
add_child(tree1, 'Guelph', weight=30, heuristic=160)

add_child(tree1, 'New Hamburg', weight=90, heuristic=110)

# Add children of guelph: Drayton
add_child(tree1['children'][0], 'Drayton', weight=100, heuristic=100)

# Children of Drayton: Listowel
add_child(tree1['children'][0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of New hamburg: Startford
add_child(tree1['children'][1], 'Startford', weight=25, heuristic=100)

# Children of stratford: St. Marys and Drayton
add_child(tree1['children'][1]['children'][0], 'St. Marys', weight=30, heuristic=130)
add_child(tree1['children'][1]['children'][0], 'Drayton', weight=200, heuristic=100)

# Add children of St. Marys: Mitchell
add_child(tree1['children'][1]['children'][0]['children'][0], 'Mitchell', weight=80, heuristic=100)

#  Add children of Mitchell: Listowel
add_child(tree1['children'][1]['children'][0]['children'][0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Add children of Drayton: Listowel
add_child(tree1['children'][1]['children'][0]['children'][1], 'Listowel', weight=100, heuristic=0) 



print("--Question 1-- \n")
print("DFS ",DFS(tree,goal_name), '\n')
print("--Question 3-- \n")
print("BFS: ",BFS(tree1,goal_name), '\n')
print("Greedy Search: ",GreedySearch(tree1,goal_name), '\n')
print("UCS: ",UCS(tree1,goal_name), '\n')





"""

        --- Explanation of results ---

Q1: DFS is similar to BFS but uses a LIFO stack instead of FIFO. When we add nodes into the frontier, it will take the
most recently added node to explore first, whereas BFS would take the "oldest" node to explore first. When we explore
Kitchener's children, we first explore Guelph and then New Hanburg, DFS then takes New hamburg and continues to  explore it
until the deepest node is reached or until the goal is met. In this case Listowel was achieved, but had the goal been Mitchell,
DFS would have exhausted the path from Stratford to Drayton to Listowel and then started searching from St. Marys.

This is also a limitation of DFS as it will expand the current node as deep as possible until it either exhausted the
depth of the path or found its goal. If it had chosed to explore New Hamburg first then Guelph, using LIFO the path 
of Guelph's depth would be explored first and a shorter final path with lower cost would have been achieved. DFS will 
always find a solution if one exists, but it is not guaranteed to be the optimal solution as we see in this case.

Q3: In my output, BFS and UCS have returned the same path and the same cost. Greedy search has returned a longer path
and a higher total cost. 

BFS and UCF may have returned the same optimal solution, but their search paths differ vastly as UCS
will always choose the path that has the lowest cost(weight/distance) and BFS will explore all possible nodes in a given
"generation" first before continuing to expand onto the next generation. 

BFS will always return the shortest path in an unweighted tree because it explores each generation (depth-level). While
in this output I do return the total cost of the path, the weights were not a factor in the code for running BFS.

The reason for greedy search returning a longer path is that it will choose the state to explore next that has the highest
immediate gain (lowest immediate cost) through its heuristic function. Since the cost of New Hamburg (110) is less than 
Guelph (160) it will explore New Hamburg first. Using this logic it will later choose Drayton over St. Mary's as it has
the lower heruistic cost and will ultiamtely arrive at the goal of Listowel. 

UCS will helps to return the path with the shortest cost as it prioritizes selecting the path with minimal cost at each 
step.



"""
