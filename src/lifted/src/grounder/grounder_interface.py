import itertools
import copy
from pddl.parser import Parser
import grounding
import sys
from Plan_Graph_Generator import PLanGraphGenerator

DOM_TEMPL = "templ_domain.pddl"
PROB_TEMPL = "templ_problem.pddl"
PRED_TEMPL = "%PREDS%"
ACTION_TEMPL = "\t(:action %NAME%"+ "\n\t\t" +":parameters ()"+"\n\t\t"+":precondition\n\t\t(and \n\t\t\t%PRECONDS%)\n\t\t:effect\n\t\t(and \n\t\t\t%POS_EFFECTS%%DEL_EFFECTS%\n\t\t)\n\t)"
INIT_TEMPL = "%INIT%"
GOAL_TEMPL = "%GOAL%"

class GROUNDER_INTERFACE(object):
    def __init__(self, domain_file, problem_file):
        """
            domain - domain pddl file
            problem - problem pddl file
        """
        #parse the domain and problem
        with open(DOM_TEMPL) as d_fd:
            self.domain_template = '\n'.join([line.strip() for line in d_fd.readlines()])
        with open(PROB_TEMPL) as p_fd:
            self.prob_template = '\n'.join([line.strip() for line in p_fd.readlines()])
        parser = Parser(domain_file, problem_file)
        domain = parser.parse_domain()
        problem = parser.parse_problem(domain)
        self.task = grounding.ground(problem)

    def de_parameterizer(self, item_list):
        final_list = []
        for item in item_list:
            tmp = '_'.join(str(item).split(' '))
            final_list.append(tmp)
        return final_list
    
    def write_to_file(self, target_domain_file, target_problem_file):
       domain = self.domain_template.replace(PRED_TEMPL, '\n'.join(self.de_parameterizer((self.task.facts))))
       action_string = ""
       for i in range(len(self.task.operators)):
           if len(self.task.operators[i].add_effects) > 0 or len(self.task.operators[i].del_effects) > 0:
                tmp_str = ACTION_TEMPL.replace('%NAME%', '_'.join(self.task.operators[i].name.replace('(','').replace(')','').split(' ')))
                tmp_str = tmp_str.replace('%PRECONDS%', '\n\t\t\t'.join(self.de_parameterizer(self.task.operators[i].preconditions)))
                tmp_str = tmp_str.replace('%POS_EFFECTS%','\n\t\t\t'.join(self.de_parameterizer(self.task.operators[i].add_effects)))
                del_str = ''
                for n in self.de_parameterizer(self.task.operators[i].del_effects):
                    del_str += '\n\t\t\t(not '+n+')'
                tmp_str = tmp_str.replace('%DEL_EFFECTS%',del_str)
                action_string += "\n" + tmp_str
       domain = domain.replace('%OPERATORS%',action_string)
       with open(target_domain_file,'w') as d_fd:
           d_fd.write(domain)
       problem =  self.prob_template.replace(INIT_TEMPL, '\n'.join(self.de_parameterizer(self.task.initial_state)))
       problem =  problem.replace(GOAL_TEMPL, '\n'.join(self.de_parameterizer(self.task.goals)))
       with open(target_problem_file,'w') as p_fd:
           p_fd.write(problem)

    def run_pg_test(self, plan):
        operator_map = {}
        for op in self.task.operators:
            operator_map[op.name] = op
        pg = PLanGraphGenerator(self.task, plan, operator_map)
        if pg.perform_fault_check():
            print ("True")
        else:
            print ("False")


if __name__ == '__main__':
    domain_file = sys.argv[1]
    problem_file = sys.argv[2]
    gi = GROUNDER_INTERFACE(domain_file, problem_file)
    if sys.argv[3] == "Test":
        plan = []
        with open(sys.argv[4]) as p_fd:
            for action in p_fd.readlines():
                if action[0] != ';':
                    plan.append(action.strip())
            gi.run_pg_test(plan)
    else:
        target_domain_file = sys.argv[3]
        target_problem_file = sys.argv[4]
        gi.write_to_file(target_domain_file, target_problem_file)
