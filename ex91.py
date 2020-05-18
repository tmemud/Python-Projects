fname = input ('enter file name : ')
if len(fname) < 1: fname = 'clown.txt'
hand = open (fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()

    wds = lin.split()

    for w in wds:
        #idioms, retrieve, create, update counter
        di[w] = di.get(w, 0) + 1

# print (di)

#to find the most common word
largest = -1
theword = none
for k,v in di.items():
    print (k, v)
    if v > largest :
        largest = v
        the word = k

print ('done', theword, largest)
