#!/usr/bin/env python

'''
Topic   :: Environment definition
Project :: Explanations for Multi-Model Planning
Author  :: Tathagata Chakraborti
Date    :: 09/29/2016
'''

from PDDLhelp import *
from Search   import astarSearch
import copy, argparse, sys

'''
Class :: Environment Definition
'''

class Problem:

    def __init__(self, robotModelFile, humanModelFile, problemFile, robotPlanFile = None):

        print "Setting up MMP..."
        
        if not robotPlanFile: self.plan, self.cost = get_plan(robotModelFile, problemFile)
        else:

            with open(robotPlanFile, 'r') as plan_file:
                temp      = plan_file.read().strip().split('\n')
                self.plan = temp[:-1]
                self.cost = int(temp[-1].split(' ')[3].strip())
            
        ground(robotModelFile, problemFile)
        self.ground_state = read_state_from_domain_file('tr-domain.pddl')

        ground(humanModelFile, problemFile)

        try:    self.initialState = read_state_from_domain_file('tr-domain.pddl')
        except: self.initialState = []
            
    def getStartState(self):
        return self.initialState

    def isGoal(self, state):

        temp_domain = write_domain_file_from_state(state)
        plan, cost  = get_plan(temp_domain, 'tr-problem.pddl')

        return cost == self.cost 

    def heuristic(self, state):
        return 0.0
    
    def getSuccessors(self, node):

        listOfSuccessors = []

        state            = set(node[0])
        ground_state     = set(self.ground_state)

        add_set          = ground_state.difference(state)
        del_set          = state.difference(ground_state)

        for item in add_set:
            new_state    = copy.deepcopy(state)
            new_state.add(item)
            listOfSuccessors.append([list(new_state), item])

        for item in del_set:
            new_state    = copy.deepcopy(state)
            new_state.remove(item)
            listOfSuccessors.append([list(new_state), item])
        
        return listOfSuccessors
        

'''
main method
'''

def main():
    
    parser = argparse.ArgumentParser(description = '''This is the Problem class. Explanations for Multi-Model Planning.''',
                                     epilog      = '''Usage >> ./Problem.py -m ../domain/fetchworld-tuck-m.pddl -n ../domain/fetchworld-base-m.pddl -f ../domain/problem1.pddl ''')
     
    parser.add_argument('-m', '--model',   type=str, help="Domain file with real PDDL model of robot.")
    parser.add_argument('-n', '--nmodel',  type=str, help="Domain file with human model of the robot.")
    parser.add_argument('-f', '--problem', type=str, help="Problem file.")
    parser.add_argument('-p', '--plan',    type=str, help="Plan file.")
 
    args             = parser.parse_args()

    if not sys.argv[1:]:
        print parser.print_help()

    problem_instance = Problem(args.model, args.nmodel, args.problem, args.plan)
    plan             = astarSearch(problem_instance)

    for item in plan:
        print 'Explanation >> ', item

if __name__ == '__main__':
    main()
