# Explanations for Multi-Model Planning (MMP)
![alt tag](logo.png)

## Try out:
### Fetch needs to tuck its arm before moving
>> \>> ./Problem.py -m ../domain/fetchworld-tuck-m.pddl -n ../domain/fetchworld-base-m.pddl -f ../domain/problem1.pddl  
Number of Nodes Expanded = 2  
Explanation >> MOVE_LOC1_LOC2-has-precondition-HAND-TUCKED  

### Fetch needs to charge after moving
>> \>> ./Problem.py -m ../domain/fetchworld-charge-sm-m.pddl -n ../domain/fetchworld-base-m.pddl -f ../domain/problem1.pddl  
Number of Nodes Expanded = 838  
Explanation >> MOVE_LOC1_LOC2-has-precondition-HAND-TUCKED  
Explanation >> MOVE_LOC2_LOC1-has-precondition-CHARGED  
Explanation >> CHARGE-has-add-effect-CHARGED  

### Fetch needs to charge after move, pickup, putdown actions
>> \>> ./Problem.py -m ../domain/fetchworld-charge-lg-m.pddl -n ../domain/fetchworld-base-m.pddl -f ../domain/problem1.pddl  
Number of Nodes Expanded = 