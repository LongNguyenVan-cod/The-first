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

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	for i in range(5,16):
		if s[i] == "-1":
			not_take_exam[i-5] += 1

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)
print(not_take_exam_percentage)
print(subject)

import matplotlib.pyplot as plt
import numpy as np
figure, axis = plt.subplots()

y_pos = np.arange(len(subject))

#Plot barchart using 2 list
plt.bar(y_pos, not_take_exam_percentage)

#Change horizontal category name
plt.xticks(y_pos, subject)

#Set limit to vertical axis
axis.set_ylim(0, 100)

# Title cua bieu do and name axis
plt.ylabel('Percentage')
plt.title('So hoc sinh bo thi hoac khong dang ky')

rects = axis.patches
# Make some labels.
labels = not_take_exam_percentage

for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
    )

plt.show()