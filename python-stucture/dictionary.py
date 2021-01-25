"""List within Dictionary """
persion = [['name', {'details': 'heme'}], [], []]

"""" Working with dictionary in list  """
employees = [
    {'name': 'kanon', 'age': 30, 'department': 'Web Development'},
    {'name': 'jamil', 'age': 31, 'department': 'HR'},
    {'name': 'rahul', 'age': 32, 'department': 'UX UI'}

]
print('Name \tAge \tDepartment')
print('-' * 30)
for info in employees:
    print(info['name'].title(), '\t', info['age'], '\t', info['department'])
    print('-' * 30)
