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

#Create list ho va so hoc sinh theo tung ho
name = []
name_count = []

for s in students:
	s_name = s[1].split(" ")
	lastname = s_name[0]
	if lastname not in name:
		name.append(lastname)
		name_count.append(0)
		name_count[name.index(lastname)] += 1
	else:
		name_count[name.index(lastname)] += 1

#Sap xep so lan lap theo tung ho tu lon den nho
counted_max_num = []
for i in range(len(name)):
	max_num = 0
	for j in range(len(name_count)):
		if name_count[j] > max_num and name_count[j] not in counted_max_num:
			max_num = name_count[j]
	counted_max_num.append(max_num)

#Delete element = 0 in counted_max_num
counted_max = []
for i in range(len(counted_max_num)):
	if counted_max_num[i] != 0:
		counted_max.append(counted_max_num[i])
counted_max_num = counted_max

#Tao danh sach chua vi tri cac ho theo so lan lap tu lon den nho
sort_index = []
for max_num in counted_max_num:
	for i in range(len(name_count)):
		if max_num == name_count[i]:
			sort_index.append(i)

#Tao danh sach ho va so lan lap tung ho theo thu tu lon den nho
name_sort = []
name_count_sort = []
for index in sort_index:
	name_sort.append(name[index])
	name_count_sort.append(name_count[index])

# print(name_sort)
# print(name_count_sort)

import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

num = 25

# Gia tri cua x va y phai bang nhau
x = np.arange(num)
y = np.arange(num)

#Plot barchart using 2 list
plt.bar(x, name_count_sort[0:num])

#Change horizontal category name
plt.xticks(x, name_sort[0:num])

#Set limit to vertical axis
axis.set_ylim(0, 25000)

# Title cua bieu do and name axis
plt.ylabel('Number of student')
plt.xlabel('Ho')
plt.title(str(num) + ' HO PHO BIEN NHAT TRONG KY THI')

rects = axis.patches
# Make some labels.
labels = name_count_sort[0:25]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
    )

plt.show()

