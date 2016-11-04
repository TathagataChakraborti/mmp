#!/usr/bin/env python

'''
Topic   :: Search methods
Project :: Explanations for Multi-Model Planning
Author  :: Tathagata Chakraborti
Date    :: 09/29/2016
'''

from Queue import Queue
import copy

'''
Method :: Astar Search
'''

def BFSearch(problem):
    
    startState            = problem.getStartState()
    fringe                = Queue()
    closed                = set()
    numberOfNodesExpanded = 0
    conflict_list = []
    current_sol = []

    fringe.put((problem.heuristic(startState), [startState, []]))

    print "Runnning BFS..."
    while not fringe.empty():
        node = fringe.get()[1]

        if problem.isGoal(node[0]):
            #print "Goal Found! Number of Nodes Expanded =", numberOfNodesExpanded
            #print "Failed for path",node[1]
            conflict_list.append(set(node[1]))
        else:

            if frozenset(node[0]) not in closed:
                conflict_flag = False
                for item in conflict_list:
                    if item <= set(node[1]) and len(item) > 0:
                        conflict_flag = True
                if not conflict_flag:
                    current_sol = node[1]
                    closed.add(frozenset(node[0]))

                    successor_list         = problem.getSuccessors(node)
                    numberOfNodesExpanded += 1

                    if not numberOfNodesExpanded % 100:
                        print "Number of Nodes Expanded =", numberOfNodesExpanded
            
                    while successor_list:
                
                        candidate_node     = successor_list.pop()
                        new_node           = [candidate_node[0], node[1] + [candidate_node[1]]]
                
                        fringe.put((problem.heuristic(candidate_node[0]) + len(new_node[1]), new_node))
    #print "conflict_list", conflict_list
    return current_sol
