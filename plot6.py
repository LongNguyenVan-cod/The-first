with open("test.csv", "r", encoding='utf-8') as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

header = header.split(",")
subject = header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")
total_student = len(students)

#Delete phan tu cuoi cung
students.pop()

#Lay do dai ten lon nhat
max_len_name = 0
for i in range(len(students)):
	if len(students[i][1]) > max_len_name:
		max_len_name = len(students[i][1])

#Tao list chua ten va danh sach thi sinh 
max_name = []
sbd_student_max_name = []
for s in students:
	if max_len_name == len(s[1]):
		max_name.append(s[1])
		sbd_student_max_name.append(s[0])

for i in range(len(max_name)):
	print(sbd_student_max_name[i] + "_" + max_name[i])

# print(students[index][0])
# print(students[index][1])
# print(len(students[index][1]))

