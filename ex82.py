#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.




fname = input("Enter file name: ") #Ask the user for the filename.
fh = open(fname)                   #Open the file.
lst = list()                       #Create a list called lst.
for line in fh:                    #For each line in the fh?
     words = line.split()        #Separate the words in the line.
     for word in words :           #For each word in words.
         if word not in lst :      #If word not in the lst.
            lst.append(word)       #Add the word.
         elif word in lst :            #Continue looping.
            continue
lst.sort()
print(lst)                         #Print the lst.
