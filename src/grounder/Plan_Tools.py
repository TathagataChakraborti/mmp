import sys
import os
import task
import copy

class PlanTools:
    def __init__(self, robot_task, plan, operator_map):
        start_action = task.Operator('init_action', frozenset(), robot_task.initial_state, frozenset())
        end_action = task.Operator('goal_action', robot_task.goals, frozenset(), frozenset())
        self.operator_map = operator_map
        self.operator_map[start_action.name] = start_action
        self.operator_map[end_action.name] = end_action
        self.new_plan = [start_action.name] + plan + [end_action.name]
    
    def perform_fault_check(self):
        fault_list = []
        contributing_actions = set()
        pos = 0
        for action in self.new_plan:
            preconds = list(self.operator_map[action].preconditions)
            old_faults = copy.deepcopy(fault_list)
            for fault in old_faults:
                faulty_action, fault_pos, fault_name = fault.split(':')
                if fault_name in preconds:
                    fault_list.pop(fault_list.index(fault))
                    preconds.pop(preconds.index(fault_name))
                    contributing_actions.add(faulty_action+fault_pos)
            add_effects = list(self.operator_map[action].add_effects)
            add_effects.sort()
            for add in add_effects:
                fault_list.append(action+':'+str(pos)+':'+add)
            pos = pos+1
        if len(contributing_actions) < len(self.new_plan) - 1 :
            return False
        return True


