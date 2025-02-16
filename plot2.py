with open("test.csv", "r", encoding='utf-8') as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

header = header.split(",")
subject = header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")

#Delete phan tu cuoi cung
students.pop()
total_student = len(students)

#Number of students took 0, 1, 2, ... subject
number_of_exam_taken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Avr diem cua cac hoc sinh thi theo 0, 1, 2, ... subject
averange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in students:
	count_subject = 0
	total = 0
	for i in range(0, 11):
		if s[i+5] != "-1":
			total += float(s[i+5])
			count_subject += 1

	number_of_exam_taken[count_subject] += 1
	averange[count_subject] += total/count_subject

for i in range(0,12):
	if number_of_exam_taken[i] != 0:
		averange[i] = round(averange[i]/number_of_exam_taken[i], 2)
	
print(averange)
print(number_of_exam_taken)

# import matplotlib.pyplot as plt
# import numpy as np

# figure, axis = plt.subplots()

# # Gia tri cua x va y phai bang nhau
# x = np.arange(len(number_of_exam_taken))
# y = np.arange(len(averange))

# #Plot barchart using 2 list
# plt.bar(x, averange)

# #Change horizontal category name
# plt.xticks(x, x)

# #Set limit to vertical axis
# axis.set_ylim(0, 10)

# # Title cua bieu do and name axis
# plt.ylabel('Averange')
# plt.title('Diem trung binh theo so mon thi')

# rects = axis.patches
# # Make some labels.
# labels = averange

# for rect, label in zip(rects, labels):
#     height = rect.get_height()
#     axis.text(
#         rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
#     )

# plt.show()

import matplotlib.pyplot as plt

labels = ['0 Mon', '1 Mon', '2 Mon', '3 Mon', '4 Mon', '5 Mon', '6 Mon', '7 Mon', '8 Mon', '9 Mon', '10 Mon', '11 Mon']
sizes = number_of_exam_taken

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.show()

