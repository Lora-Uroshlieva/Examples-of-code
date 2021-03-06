new_studs = []

while 1:
    student = input('Enter name of student: ').strip().capitalize()
    if not student:
        continue
    if student.lower() == 'exit':
        break
    new_studs.append(student)

print(new_studs)


# Find maximum and minimum from list using loop.

my_list = [1, 8, 6, 13, 0, 6, 2, -3, -9]
maximum = my_list[0]
minimum = my_list[0]
for item in my_list:
    if item > maximum:
        maximum = item
    if item < minimum:
        minimum = item

print('maximum is: ', maximum, 'minimum is: ', minimum)


# Find even, odd numbers from list

first_list = [1, 4, 5, 7, 2, 2, 9, 22, 45, 10, 3, 5, 46]
even = []
odd = []
for item in first_list:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)
print('Even: ', even)
print('Odd', odd)


# multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print('%s * %s = %s' % (i, j, i*j))
    print('-'*10)

# stairs from stars
for i in range(6):
    print('*'*i)

#stairs from digits:
for i in range(6):
    print(str(i)*i)


#sum of digits in string
my_string = 'lhjkh11111lkjkl88'
total = 0
for item in my_string:
    if item.isdigit():
        total += int(item)

print('Sum is: ', total)


# delete from list elements with length >5
list_3 = ['111', 'aaaaaaaaaaa', 'bbbbb', 'c', 'dddddd']
list_modified = []
for item in list_3:
    if len(item)<6:
        list_modified.append(item)

print(list_modified)


# Print array from list
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
