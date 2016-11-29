#!/usr/bin/env python

'''
Topic   :: Random Problem Generator
Project :: Explanations for Multi-Model Planning
Date    :: 11/15/2016
'''

from PDDLhelp import *
import copy, argparse, os, sys
import numpy as np
import time
import random

'''
Class :: Environment Definition
'''

class RandomDomainGenerator:

    def __init__(self, original_domain):
        self.original_domain = original_domain
        self.domain_as_state = read_state_from_domain_file(original_domain) 
        
    def getRandomDomain(self, target_file, diff_count, domain_src):
        current_diff = 0
        rand_obj = np.random.RandomState()
        if (diff_count >= len(self.domain_as_state)):
            print "The Change count is too Damn High...."
            exit(1)
        new_state = copy.deepcopy(self.domain_as_state)
        rand_obj.shuffle(new_state)
        dlt_cnt = 0
        curr_id = 0
        delete_choices = []
        while dlt_cnt < diff_count:
            if curr_id == len(self.domain_as_state):
                curr_id = 0
            if 'parameter' not in new_state[curr_id]:
                if "precondition" not in new_state[curr_id]:
                    if new_state[curr_id] not in delete_choices:
                        delete_choices.append(new_state[curr_id])
                        dlt_cnt += 1
                else:
                    action, pred = new_state[curr_id].split('-has-precondition-')
                    if '{}-has-delete-effect-{}'.format(action, pred) not in new_state:
                        delete_choices.append(new_state[curr_id])
                        dlt_cnt += 1

            curr_id += 1

        for del_item in delete_choices:
            self.domain_as_state.pop(self.domain_as_state.index(del_item))
        write_domain_file_from_state(self.domain_as_state, target_file, domain_src)
        

'''
main method
'''

def main():
    
    parser = argparse.ArgumentParser(description = '''This is the Problem class. Explanations for Multi-Model Planning.''',
                                     epilog      = '''Usage >> ./RandomDomGen.py -m ../domain/fetchworld-tuck-m.pddl -t /tmp/test -c 5''')
     
    parser.add_argument('-m', '--model',   type=str, help="Original domain file.")
    parser.add_argument('-t', '--tmodel',  type=str, help="Target domain file")
    parser.add_argument('-d', '--domain_templ',  type=str, help="Domain template file")
    parser.add_argument('-c', '--count', type=str, help="Number of domain changes")
 
    args   = parser.parse_args()

    if not sys.argv[1:]:
        print parser.print_help()

    else:
        
        gen_instance = RandomDomainGenerator(args.model)
        gen_instance.getRandomDomain(args.tmodel, int(args.count), args.domain_templ)

if __name__ == '__main__':
    main()
