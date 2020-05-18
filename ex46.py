#average in  a loop
count=0
sum=0
for other_numbers in [1,2,3,4,5,6,7,8,]:
    count= count + 1
    sum= sum + other_numbers
    print(count, other_numbers, sum)
print(count, other_numbers, sum/count)
