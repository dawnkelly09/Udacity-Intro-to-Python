#input: will display on screen for user to type in info
#title: capitalization of the names
#split: dividing string of input into a list of objects at each comma
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

#assign the message variable to the message to print
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

#for loop: for each name, assignment, and grade in each list
    #zip: matches items together that are in the same index location on the lists
    #zip: think of it like collating a multi page document
#print: print the message with variables plugged in
#message.format--use the message string and plug in these variables in {}
#int(assignment)*2 formula from problem background info 
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
