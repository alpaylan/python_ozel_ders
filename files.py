f = open("recursion.py", "r")
lines = f.read().split("\n")
f2 = open("recursion_copy.py", "w")
for line in lines:

    f2.write(line + "\n")

    if len(line) > 0 and line[0] == "#":
        continue
    print(line)

# r -> read
# w -> write from beginning
# a -> append
# x -> create
