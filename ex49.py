#findiong the smallest vbalue

smallest = None
print ('before')
for numbers in [1,2,3,4,5,6,7,8,9] :
    if smallest is None:
        smallest = numbers
    elif numbers < smallest:
        smallest= numbers
    print(smallest, numbers)
print("after", smallest)
