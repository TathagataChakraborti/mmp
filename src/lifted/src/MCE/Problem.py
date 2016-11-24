#!/usr/bin/env python

'''
Topic   :: Environment definition
Project :: Explanations for Multi-Model Planning
Author  :: Tathagata Chakraborti
Date    :: 09/29/2016
'''

from PDDLhelp import *
from Search   import BFSearch
import copy, argparse, os, sys

'''
Class :: Environment Definition
'''

class Problem:

    def __init__(self, robotModelFile, humanModelFile, problemFile, domainTemplate, robotPlanFile = None):

        print "Setting up MMP..."
        self.domainTemplate = domainTemplate

        if not robotPlanFile:

            self.robotPlanFile   = '../../domain/cache_plan.dat'
            self.plan, self.cost = get_plan(robotModelFile, problemFile)

            with open(self.robotPlanFile, 'w') as plan_file:
                plan_file.write('\n'.join(['({})'.format(item) for item in self.plan]) + '\n; cost = {} (unit cost)'.format(self.cost))
            
        else:

            self.robotPlanFile   = robotPlanFile
            with open(robotPlanFile, 'r') as plan_file:
                temp      = plan_file.read().strip().split('\n')
                self.plan = temp[:-1]
                self.cost = int(temp[-1].split(' ')[3].strip())
            
        ground(humanModelFile, problemFile)
        self.ground_state = read_state_from_domain_file('tr-domain.pddl')
        self.human_model = copy.copy(self.ground_state)
        ground(robotModelFile, problemFile)

        self.robotPlanFile   = '../../domain/cache_plan.dat'
        self.plan, self.cost = get_plan('tr-domain.pddl', 'tr-problem.pddl')

        with open(self.robotPlanFile, 'w') as plan_file:
            plan_file.write('\n'.join(['({})'.format(item) for item in self.plan]) + '\n; cost = {} (unit cost)'.format(self.cost))
 


        try:    self.initialState = read_state_from_domain_file('tr-domain.pddl')
        except: self.initialState = []
        #print "initial state is",self.initialState
        #print "add set",set(self.ground_state) - set(self.initialState)
        #print "del set",set(self.initialState) - set(self.ground_state)
        #exit()

    def getStartState(self):
        return self.initialState

    def isGoal(self, state):

        temp_domain      = write_domain_file_from_state(state, self.domainTemplate)
        plan, cost       = get_plan(temp_domain, 'tr-problem.pddl')
        optimality_flag  = cost < self.cost
        
        feasibility_flag = not validate_plan(temp_domain, 'tr-problem.pddl', self.robotPlanFile)
        
        return optimality_flag or feasibility_flag

    
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
    parser.add_argument('-d', '--domain_template',   type=str, help="Domain template for the current MMP.")
    parser.add_argument('-f', '--problem', type=str, help="Problem file.")
    parser.add_argument('-p', '--plan',    type=str, help="Plan file.")
 
    args   = parser.parse_args()

    if not sys.argv[1:]:
        print parser.print_help()

    else:
        
        problem_instance = Problem(args.model, args.nmodel, args.problem, args.domain_template, args.plan)
        k_plan             = BFSearch(problem_instance)
        #print "k_plan ",k_plan
        #print "add items", ((set(problem_instance.initialState) - set(problem_instance.human_model)))
        #print "del items", ((set(problem_instance.human_model) - set(problem_instance.initialState)))
        plan = ((set(problem_instance.initialState) - set(problem_instance.human_model))|(set(problem_instance.human_model) - set(problem_instance.initialState)))- set(k_plan)
        explanation      = ''
        for item in plan:
            explanation += "Explanation >> {}\n".format(item)

        print explanation.strip()
        with open('exp.dat', 'w') as explanation_file:
            explanation_file.write(explanation.strip())
        

if __name__ == '__main__':
    main()
