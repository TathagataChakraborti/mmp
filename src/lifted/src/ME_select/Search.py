#!/usr/bin/env python

'''
Topic   :: Search methods
Project :: Explanations for Multi-Model Planning
Author  :: Tathagata Chakraborti
Date    :: 09/29/2016
'''

from Queue import PriorityQueue
import copy

'''
Method :: Astar Search
'''

def astarSearch(problem):
    
    startState            = problem.getStartState()
    fringe                = PriorityQueue()
    closed                = set()
    numberOfNodesExpanded = 0

    fringe.put((problem.heuristic(startState), [startState, []]))

    print "Runnning aStar Search..."
    while not fringe.empty():
        
        node = fringe.get()[1]
        goal_status, old_plan = problem.isGoal(node[0])
        if goal_status:
            print "Goal Found! Number of Nodes Expanded =", numberOfNodesExpanded
            return node[1]

        if frozenset(node[0]) not in closed:

            closed.add(frozenset(node[0]))

            successor_list         = problem.getSuccessors(node, old_plan)
            numberOfNodesExpanded += 1

            if not numberOfNodesExpanded % 100:
                print "Number of Nodes Expanded =", numberOfNodesExpanded
            
            while successor_list:
                
                candidate_node     = successor_list.pop()
                new_node           = [candidate_node[0], node[1] + [candidate_node[1]]]
                
                fringe.put((problem.heuristic(candidate_node[0]) + len(new_node[1]), new_node))

    return None
