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
        
    def getRandomDomain(self, target_file, diff_count):
        current_diff = 0
        rand_obj = np.random.RandomState()
        if (diff_count >= len(self.domain_as_state)):
            print "The Change count is too Damn High...."
            exit(1)
        delete_choices = rand_obj.choice(self.domain_as_state, diff_count)
        for del_item in delete_choices:
            self.domain_as_state.pop(self.domain_as_state.index(del_item))
        write_domain_file_from_state(self.domain_as_state, target_file)
        

'''
main method
'''

def main():
    
    parser = argparse.ArgumentParser(description = '''This is the Problem class. Explanations for Multi-Model Planning.''',
                                     epilog      = '''Usage >> ./RandomDomGen.py -m ../domain/fetchworld-tuck-m.pddl -t /tmp/test -c 5''')
     
    parser.add_argument('-m', '--model',   type=str, help="Original domain file.")
    parser.add_argument('-t', '--tmodel',  type=str, help="Target domain file")
    parser.add_argument('-c', '--count', type=str, help="Number of domain changes")
 
    args   = parser.parse_args()

    if not sys.argv[1:]:
        print parser.print_help()

    else:
        
        gen_instance = RandomDomainGenerator(args.model)
        gen_instance.getRandomDomain(args.tmodel, int(args.count))

if __name__ == '__main__':
    main()
