# Use the file name mbox-short.txt as the file name

#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
 #looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt



#when you are testing below enter mbox-short.txt as the file name.
#Average spam confidence: 0.750718518519


fname = input("Enter file name: ")
fh = open(fname)

count = 0
add = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    sval = line.find(":")
    numbers = line[sval+2 : ]
    fval = float (numbers)
    add += fval
    count += 1

average = add/count
print("Average spam confidence:", average)

    #count = count + 1
    #print(count)






    #print(line)
    #print (count)
#print("Done")
