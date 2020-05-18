
fh = open ('mbox-short.txt')

for line in fh:
    liney = line.rstrip()
    print (liney.upper())
