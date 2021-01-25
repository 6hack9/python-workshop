s5 = {1,2,3,4}
s6 = {3,4,5,6}

""" Use the | operator or the union method for a union operation: """

print(s5 | s6, '\n')

print(s5.union(s6),'\n')

""" Now use the & operator or the intersection method for an intersection operation: """

print(s5 & s6, '\n') 

print(s5.intersection(s6),'\n')

""" Use the – operator or the difference method to find the difference between two sets: """

print(s5 -s6, '\n')

print(s5.difference(s6),'\n')

"""  Now enter the <= operator or the issubset method to check if one set is a subset of another: """

print((s5 <= s6))

print(s5.issubset(s6),'\n')
s7 = {1,2,3}
s8 = {1,2,3,4,5}

print(s7 <= s8)

print(s7.issubset(s8))