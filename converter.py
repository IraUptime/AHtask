import csv 

file = open('input.csv', 'r')

reader = csv.reader(file)
lines_counter = 0
print(reader)
print("begin of reading file:")
for row in reader:
     lines_counter = lines_counter +1
     print ("line nr: %d " % lines_counter) 
     print(row)

print("This is the end!")




