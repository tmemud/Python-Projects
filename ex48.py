#serch using a boolean variable
found = False
print ('before', found)
for numbers in [1,2,3,4,5,6] :
    if numbers == 3:
        found = True
        print (found, numbers)
print ('after', found)
