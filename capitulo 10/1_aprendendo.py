filename = "learning_python.txt"

with open(filename) as learning:
    lear = learning.read()
    print(lear)
    
print("-----------------")

with open(filename) as learning:
    for lear in learning:
        print(lear.rstrip())

print("-----------------")

with open(filename) as learning:
    line = learning.readlines()
    
for lear in line:
    print(lear.rstrip())