initial_number = 2
print ('largest so far', initial_number)
for new_numbers in [1,3,4,5,7,8,9,0] :
  if new_numbers > initial_number :
    initial_number = new_numbers
    print (initial_number, new_numbers)

print("finfish")
