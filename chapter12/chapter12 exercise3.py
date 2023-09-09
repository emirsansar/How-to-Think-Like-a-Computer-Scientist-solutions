#Investigate the copy module. What does deepcopy do? In which exercises from last chapter would deepcopy have come in handy?

import copy

list = [1,2,3,[4,5]]

list_2 = copy.deepcopy(list)

list_2[2] = 9

print(list)

print(list_2)

# deepcopy function ensures that the original list remains unchanged.