"""
Original solution by Sujin Lee

https://www.hackerrank.com/challenges/finding-the-percentage

"""

#number of students
n = input()
 
# list of sujects
subject = ['Name', 'Maths', 'Physics', 'Chemistry']
 
# make data table
while n > 0:
    n -= 1
    data = raw_input().split(" ")
    name = data[0]
    print name
    for i in range(len(data)):
       
        result = dict(zip(subject, data))
   
    name = result
    print name
 
# find a student's data
findname = raw_input()
if findname in name:
    print "YES"
else:
    print "NO"