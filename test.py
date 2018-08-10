file = open("test.txt")
for line in file:
    if not line.isspace():
        print(line[0])
        