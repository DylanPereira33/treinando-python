filename = "learning_python.txt"

with open(filename) as learning:
    lear = learning.read()
    print(lear.replace("Python", "C"))