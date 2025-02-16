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

#So hoc sinh theo do tuoi
number_student_per_of_age = [0,0,0,0,0,0,0,0,0,0,0]
averange_student_per_of_age = [0,0,0,0,0,0,0,0,0,0,0]
number_of_age = ['17','18','19','20','21','22','23','24','25','26','>26']

for s in students:
	age = 2020 - int(s[4])
	if age >= 27:
		age = 27
	number_student_per_of_age[age-17] += 1
	sum_scores = 0
	count_subject = 0
	for i in range(0,11):
		if s[i+5] != "-1":
			sum_scores += float(s[i+5])
			count_subject += 1
	averange = round(sum_scores/count_subject, 2)
	averange_student_per_of_age[age-17] += averange

for i in range(len(averange_student_per_of_age)):
	averange_student_per_of_age[i] = round(averange_student_per_of_age[i]/number_student_per_of_age[i], 2)

#Scale list diem trung binh theo thang do
for i in range(len(averange_student_per_of_age)):
	averange_student_per_of_age[i] = averange_student_per_of_age[i]*(70000/10)

# print(averange_student_per_of_age)
# print(number_student_per_of_age)

#Them vao thu vien
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

x_axis = np.arange(len(number_student_per_of_age))

#Plot barchart using 2 list
plt.bar(x_axis, number_student_per_of_age)
plt.plot(x_axis, averange_student_per_of_age, color='red', marker='o')

#Change horizontal category name
plt.xticks(x_axis, number_of_age)

#Set limit to vertical axis
axis.set_ylim(0, 70000)

# Title cua bieu do and name axis
plt.ylabel('Number of student')
plt.xlabel('Age')
plt.title('Diem trung binh theo do tuoi')

#right side ticks
ax2 = axis.twinx()
ax2.tick_params('y', color='r')
ax2.set_ylim(0,10)
ax2.set_ylabel('Averange scores', color='r')

rects = axis.patches
# Make some labels.
labels = number_student_per_of_age

for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
    )

plt.show()