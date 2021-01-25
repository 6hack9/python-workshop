shoplist = ['Laptop', 'Big Monitor', 'Table', 'Earphone']
# print(shoplist)

# Runing loop through List
for item in shoplist:
    print('I will have to buy ', item)

# Nested List in Matrix
""" for nested Matrix we need to work with nested Loop
for row in m:
    for col in row:
        prin(col)
"""
# m = [[1,2,3],[4,5,6]]
# for row in range(len(m)):
#         for col in range(len(m[row])):
#          print(m[row][col])

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print('\n', m1, '\n')
for x in range(len(m1)):
    #print('x =',x )
    for y in range(len(m1[x])):
        print('row : {}\t column index : {}  \tcolumn value : {}'.format(
            x, y, m1[x][y]))


"""Now let's work with list CRUD(Create Read Update Delete) functions """
# Create Function

active_users = ['kanon', 'rahul', 'sopoth', 'mohan']

inactive_users = []
active_users.append('maheru')
active_users.append('tipu')

# Read Function
for activUser in active_users:
    print(activUser)

# update Function

""" Let's update maheru to rayhan"""

active_users[4] = 'rayhan'
print('\n udated active user list is: ', active_users)

# Now update list by inserting item in the begaining of the list

active_users.insert(0, 'admin')
print('\n after insetting admin', active_users, '\n')

"""Now we are going to work with delete, so let first view users index as well as value """

for index, user in enumerate(active_users):
    print('\t username:  {}  \tindex value: {}'.format(user, index))

"""" we have got below output
     username:  admin  	index value: 0
	 username:  kanon  	index value: 1
	 username:  rahul  	index value: 2
	 username:  sopoth  index value: 3
	 username:  mohan  	index value: 4
	 username:  rayhan  index value: 5
	 username:  tipu  	index value: 6
"""
del active_users[0]  # admin will be deleted for the list
print(active_users, '\n')
# now we are going to delete last item form the list and add to the inactive list

tipu = active_users.pop()  # tipu will be deleted

print(active_users)
print(tipu)

mohan = active_users.pop(3)  # mohan will be deleted

print(active_users)

""" now lets add tipu and mohan to the inactive list """

inactive_users.append(tipu)
inactive_users.append(mohan)

print('\n', inactive_users)
