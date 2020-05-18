#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number,
#catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.


#desire output is
#Invalid input
#Maximum is 10
#Minimum is 2

largest = None
smallest = None

while True :
    sval = input("Enter a number: ")
    if sval=='done':
        break
    try:
        fval = float (sval)
    except:
        print ("invalid input")
        continue
    if largest is None:
        largest = fval
    elif fval > largest :
        largest = fval

    if smallest is None:
        smallest = fval
    elif fval < smallest :
        smallest = fval

print ("maximum is ", int(largest))
print ("minimum is", int(smallest))
