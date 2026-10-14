

Students = {"udyaansh":85,"riya":87,"dev":74,"soniya":94,"pankaj":89}
print(Students)

Class_Total = 0
for score in Students.values():
    Class_Total= score + Class_Total

number_of_Students = len(Students)

avg = Class_Total/number_of_Students
print("Class Average:",avg)

highest = max(Students.values())
lowest = min(Students.values())

print("Lowest Score:",lowest)
print("Highest Score:",highest)

Students_Name = input("Enter Student Name").lower()

score = Students.get(Students_Name)


if score == None:
    print("Student does not exist")
else:
    print("Student score is:",score)



