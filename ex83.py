


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
han = open (fname)
count = 0
for line in han :
    line = line.rstrip()
    wds = line.split()

    if not line.startswith("From:") : continue
    sval = line.find("From:")
    numbers = line[sval+6 : ]

    print(numbers)
    count += 1


print("There were", count, "lines in the file with From as the first word")
