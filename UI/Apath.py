import numpy as np
from heapq import *  # pylint: disable=unused-wildcard-import



def astar(table, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given table"""

    # Create start and end node
    start_node = table[start[0]][start[1]]
    start_node.g = start_node.h = start_node.f = 0
    end_node = table[end[0]][end[1]]
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append((current.row,current.col))
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position #check
            node_position = (current_node.row + new_position[0], current_node.col + new_position[1])

            # Make sure within range
            if node_position[0] > (len(table) - 1) or node_position[0] < 0 or node_position[1] > (len(table[len(table)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if table[node_position[0]][node_position[1]].field_type == 3:
                continue

            # Create new node
            table[node_position[0]][node_position[1]].parent = current_node
            #new_node = table[node_position[0]][node_position[1]]
            print("Dla :",node_position[0],node_position[1],"rodzicem jest:",current_node.row,current_node.col)

            # Append
            children.append(table[node_position[0]][node_position[1]])

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.row - end_node.row) ** 2) + ((child.col - end_node.col) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

class AStarNode():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def APath(table, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given table"""

    # Create start and end node
    start_node = AStarNode(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = AStarNode(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(table) - 1) or node_position[0] < 0 or node_position[1] > (len(table[len(table)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if table[node_position[0]][node_position[1]].field_type == 3:
                continue

            # Create new node
            new_node = AStarNode(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
