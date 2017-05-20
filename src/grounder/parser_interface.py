import itertools
import copy
from pddl.parser import Parser
import sys

class PARSER_INTERFACE(object):
    def __init__(self, domain_file, problem_file):
        """
            domain - domain pddl file
            problem - problem pddl file
        """
        #parse the domain and problem
        parser = Parser(domain_file, problem_file)
        domain = parser.parse_domain()
        self.problem = parser.parse_problem(domain)

    def print_init_state(self):
        print ("\n".join([i.name+" "+" ".join([a for a,b in i.signature]) for i in self.problem.initial_state]))


    def print_goal_state(self):
        #print ("\n".join(list(self.problem.goal)))
        print ("\n".join([i.name+" "+" ".join([a for a,b in i.signature]) for i in self.problem.goal]))

if __name__ == '__main__':
    domain_file = sys.argv[1]
    problem_file = sys.argv[2]
    pi = PARSER_INTERFACE(domain_file, problem_file)
    if sys.argv[3] == "init":
       pi.print_init_state()   
    elif sys.argv[3] == "goal":
       pi.print_goal_state()

