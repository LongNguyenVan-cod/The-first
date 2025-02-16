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

#Danh sach ten cua cac thi sinh
name = []
#Danh sach so thi sinh cung ten
name_count = []

for s in students:
	s_name = s[1].split(" ")
	fristname = s_name[-1]
	if fristname not in name:
		name.append(fristname)
		name_count.append(0)
		name_count[name.index(fristname)] += 1
	else:
		name_count[name.index(fristname)] += 1

#Tao danh sach so lan lap cua cac ten theo thu tu lon den nho
counted_max_num = []
for i in range(len(name_count)):
	max_num = 0
	for j in range(len(name_count)):
		if name_count[j] > max_num and name_count[j] not in counted_max_num:
			max_num = name_count[j]
	counted_max_num.append(max_num)

#Delete phan tu 0 trong danh sach
count_max = []
for i in range(len(counted_max_num)):
	if counted_max_num[i] != 0:
		count_max.append(counted_max_num[i])
counted_max_num = count_max

#Lay vi tri cua tung lan lap cac ten thi sinh
sorted_index = []
for max_num in counted_max_num:
	for i in range(len(name_count)):
		if max_num == name_count[i]:
			sorted_index.append(i)

#Tao danh sach ten va so lan lap theo thu tu lon den nho
name_sorted = []
name_count_sorted = []
for index in sorted_index:
	name_sorted.append(name[index])
	name_count_sorted.append(name_count[index])

# print(name_sorted[0])
# print(sum(name_count_sorted))

import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

num = 10

# Gia tri cua x va y phai bang nhau
x = np.arange(num)
y = np.arange(num)

#Plot barchart using 2 list
plt.bar(x, name_count_sorted[0:num])

#Change horizontal category name
plt.xticks(x, name_sorted[0:num])

#Set limit to vertical axis
axis.set_ylim(0, 3500)

# Title cua bieu do and name axis
plt.ylabel('Number of student')
plt.xlabel('Name')
plt.title(str(num) + ' TEN PHO BIEN NHAT TRONG KY THI')

rects = axis.patches
# Make some labels.
labels = name_count_sorted[0:num]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
    )

plt.show()


