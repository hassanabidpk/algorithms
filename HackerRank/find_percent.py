"""
Original solution by Sujin Lee

https://www.hackerrank.com/challenges/finding-the-percentage

"""

#number of students
n = input()
studentsDict = dict()
 
# list of sujects
subject = ['Name', 'Maths', 'Physics', 'Chemistry']
 
# make data table
while n > 0:
    n -= 1
    data = raw_input().split(" ")
    name = data[0]
    score = (data[1],data[2],data[3])
    studentsDict[name] = score
    print name
    # for i in range(len(data)-1):
       
        # result = dict(zip(subject, data))


   
    print "dict : ", studentsDict
    # name = result
    # print name
 
# find a student's data
findname = raw_input()
total_score = 0
for i in range(3):
	total_score += float(studentsDict[findname][i])
	print total_score

average_score = total_score/3.0
print "average Score : " + str(average_score)
# if findname in name:
#     print "YES"
# else:
#     print "NO"