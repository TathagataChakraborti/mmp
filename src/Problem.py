#!/usr/bin/env python

'''
Topic   :: Environment definition
Project :: Explanations for Multi-Model Planning
Author  :: Tathagata Chakraborti
Date    :: 09/29/2016
'''

from PDDLhelp import *
from Search   import *
import copy

'''
Class :: Environment Definition
'''

class Problem:

    def __init__(self, robotModelFile, humanModelFile, robotProblemFile, domainTemplate,
                 ground_flag, approx_flag, heuristic_flag,
                 problemTemplate, humanProblemFile=None, robotPlanFile=None):

        print "Setting up MMP..."

        if humanProblemFile == None:
            humanProblemFile = robotProblemFile


        self.domainTemplate = domainTemplate
        self.problemTemplate = problemTemplate
        self.approx_flag = approx_flag
        self.heuristic_flag = heuristic_flag
        self.ground_flag = ground_flag

        if not robotPlanFile:
            self.robotPlanFile   = '../domain/cache_plan.dat'
            self.plan, self.cost = get_plan(robotModelFile, robotProblemFile)

            with open(self.robotPlanFile, 'w') as plan_file:
                if self.ground_flag:
                    plan_file.write('\n'.join(['({})'.format(item.replace(' ', '_')) for item in self.plan]) + '\n; cost = {} (unit cost)'
                                    .format(self.cost))
                else:
                    plan_file.write('\n'.join(['({})'.format(item) for item in self.plan]) + '\n; cost = {} (unit cost)'
                                    .format(self.cost))
        else:
            self.robotPlanFile   = robotPlanFile
            with open(robotPlanFile, 'r') as plan_file:
                temp      = plan_file.read().strip().split('\n')
                self.plan = temp[:-1]
                self.cost = int(temp[-1].split(' ')[3].strip())



        self.groundedRobotPlanFile   = '../domain/cache_grounded_plan.dat'

        with open(self.groundedRobotPlanFile, 'w') as plan_file:
            plan_file.write('\n'.join(['({})'.format(item) for item in self.plan]) + '\n; cost = {} (unit cost)'
                            .format(self.cost))

        if self.ground_flag:
            ground(robotModelFile, robotProblemFile)
            self.robot_state = read_state_from_domain_file('tr-domain.pddl','tr-problem.pddl')
            ground(humanModelFile, humanProblemFile)
            self.human_state = read_state_from_domain_file('tr-domain.pddl','tr-problem.pddl')
        else:
            self.robot_state = read_state_from_domain_file(robotModelFile, robotProblemFile)
            self.human_state = read_state_from_domain_file(humanModelFile, humanProblemFile)

        if self.approx_flag:
            if self.ground_flag:
                ground(humanModelFile, humanProblemFile)
            else:
                create_temp_files(humanModelFile, humanProblemFile)
            self.groundedHumanPlanFile = '../../domain/cache_human_grounded_plan.dat'
            grounded_human_plan, self.human_grounded_plan_cost = get_plan('tr-domain.pddl', 'tr-problem.pddl')
            self.grounded_human_plan =  set([i for i in grounded_human_plan])

    def MeSearch(self):
        self.initialState = copy.copy(self.human_state)
        self.goalState = copy.copy(self.robot_state)
        plan = astarSearch(self)
        return plan

    def MCESearch(self):

        self.initialState = copy.copy(self.robot_state)
        self.goalState = copy.copy(self.human_state)
        k_plan = BFSearch(self)
        #print set(k_plan)
        #print ((set(self.initialState) - set(self.human_state))| (set(self.human_state) - set(self.initialState)))
        return list(((set(self.initialState) - set(self.human_state))| (set(self.human_state) - set(self.initialState)))
                    - set(k_plan))

    def getStartState(self):
        return self.initialState

    def isGoal(self, state):
        if self.approx_flag:
            return self.approx_isGoal(state)
        return self.orig_isGoal(state)

    def orig_isGoal(self, state):
        temp_domain, temp_problem = write_domain_file_from_state(state, self.domainTemplate, self.problemTemplate)
        feasibility_flag = validate_plan(temp_domain, temp_problem, self.groundedRobotPlanFile)
        if not feasibility_flag:
            plan = []
            if self.heuristic_flag:
                plan, cost = get_plan(temp_domain, temp_problem)
            return (False, plan)

        plan, cost       = get_plan(temp_domain, temp_problem)
        optimality_flag  = cost == self.cost
        return (optimality_flag, plan)

    def approx_isGoal(self, state):
        temp_domain, temp_problem = write_domain_file_from_state(state,  self.domainTemplate, self.problemTemplate)

        if not validate_plan(temp_domain, temp_problem, self.groundedRobotPlanFile):
            #fail_pos = find_fail_point(temp_domain, temp_problem, self.groundedRobotPlanFile)
            return (False, list(self.plan)) #[ : min(fail_pos + 1 ,len(self.grounded_robot_plan) ) ])

        if self.human_grounded_plan_cost > 0 and self.human_grounded_plan_cost <= self.cost and \
                validate_plan(temp_domain, temp_problem, self.groundedHumanPlanFile):
            return (False, self.plan)

        graph_test_result = plan_graph_test(temp_domain, temp_problem, self.groundedRobotPlanFile)
        return (graph_test_result, self.plan)
    
    def heuristic(self, state):
        return 0.0

    
    def getSuccessors(self, node, old_plan = None):
        if self.heuristic_flag:
            return self.heuristic_successors(node, old_plan)
        return self.ordinary_successors(node)

    def ordinary_successors(self, node):

        listOfSuccessors = []

        state            = set(node[0])
        ground_state     = set(copy.copy(self.goalState))

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


    def heuristic_successors(self, node, old_plan):
        listOfSuccessors = []

        state = set(node[0])
        ground_state = set(self.robot_state)

        all_relevent_actions = set([i.lower().split()[0] for i in old_plan]) | set(
        [j.lower().split()[0] for j in self.plan])

        add_set = ground_state.difference(state)
        del_set = state.difference(ground_state)

        for item in add_set:
            if item.split('-has-')[0].lower() in all_relevent_actions:
                new_state = copy.deepcopy(state)
                new_state.add(item)
                listOfSuccessors.append([list(new_state), item])

        for item in del_set:
            if item.split('-has-')[0] in all_relevent_actions:
                new_state = copy.deepcopy(state)
                new_state.remove(item)
                listOfSuccessors.append([list(new_state), item])

        return listOfSuccessors
