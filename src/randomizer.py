import sys

from PDDLhelp import *
import random

dom_file = sys.argv[1]
count = int(sys.argv[2])
dst_templ_file =  sys.argv[3]
dst_dom_file = sys.argv[4]

state = read_state_from_domain_only_file(dom_file)

random.shuffle(state)

assert len(state) > count, "The number of elements to be removed should be less"

new_state = []
new_cnt = 0
for pred in state:
    if new_cnt >= count:
        new_state.append(pred)
    else:
        if 'parameter' not in pred and 'init' not in pred and 'goal' not in pred:
            new_cnt += 1
        else:
            new_state.append(pred)

assert new_cnt >= count, "There isn't enough non parameter elements to remove from the domain"
write_domain_only_file_from_state(new_state, dst_templ_file, dst_dom_file)
