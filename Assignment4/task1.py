filname = "semple.txt"
try:
    with open(filname, "rt") as fh:
        for line in fh:
            print(line)
except:
    print(f"File {filname} does not exist")