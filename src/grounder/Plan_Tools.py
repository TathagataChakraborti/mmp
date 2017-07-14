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
    
    def perform_contribution_check(self):
        effect_list = []
        contributing_actions = set()
        pos = 0
        for action in self.new_plan:
            preconds = list(self.operator_map[action].preconditions)
            del_lists = list(self.operator_map[action].del_effects)
            old_eff = copy.deepcopy(effect_list)
            for eff in effect_list:
                eff_action, eff_pos, eff_name = eff.split(':')
                if eff_name in del_lists:
                    effect_list.pop(effect_list.index(eff))
                elif eff_name in preconds:
                    effect_list.pop(effect_list.index(eff))
                    preconds.pop(preconds.index(eff_name))
                    contributing_actions.add(eff_action+eff_pos)
            add_effects = list(self.operator_map[action].add_effects)
            add_effects.sort()
            for add in add_effects:
                effect_list.append(action+':'+str(pos)+':'+add)
            pos = pos+1
        if len(contributing_actions) < len(self.new_plan) - 1 :
            return False
        return True


