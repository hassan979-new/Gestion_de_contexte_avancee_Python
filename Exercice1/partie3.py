from contextlib import ExitStack

paths =["Exercice1/a.txt","Exercice1/b.txt","Exercice1/c.txt"]

with ExitStack() as stack:
    files = [stack.enter_context(open(p,"w")) for p in paths]
    for f in files:
        f.write("test\n")