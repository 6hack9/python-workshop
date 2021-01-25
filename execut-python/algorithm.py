""" algorithm to find maximum number
1) set maximum number to 0
2) for each number in the list check whether the number is bigger than the maximum
3) Set the maximum variable to the given number if the given number in the list is greater than the current value of the maximum variable, else keep the maximum variable unchanged
4) Repeat this process till all the numbers in the list are done. The maximum variable is now equal to the largest number in the list.
"""
maximum = 0
numbers = [8, 5, 7, 10]

for number in numbers:
    if number > maximum:
        maximum = number

print("Gretest number is:", maximum)

""" Now let find the most small number by the user given number """

small = 3

for number in numbers:
    if number < small:
        small = number
print("small number is: ", small)


# bubble sorting

l = [5, 8, 7, 3, 1, 2, 4, 6]
print(l)
still_swap = True
while still_swap:
    still_swap = False
    for i in range(len(l) - 1):
       # print('l[i] = {} l[i+1]= {} list= {}'.format(l[i], l[i+1], l))

        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]

            still_swap = True

print(l)

# Linear Search

contacts = [5, 8, 1, 3, 2]

search = 9
suc = -1
for i in range(len(contacts)):
    if contacts[i] == search:
        suc = i
        break


print('Number Found: ', contacts[suc])

# Binary Search

l = [2, 3, 5, 8, 11, 12, 18]
search_for = 11
slice_start = 0
slice_end = len(l) - 1
found = False

while slice_start <= slice_end and not found:
    location = (slice_start + slice_end) // 2
    if l[location] == search_for:
        found = True
    else:
        if search_for < l[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1

print(found)
print(location)
