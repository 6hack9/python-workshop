""" the python language follows the same order
in the math world
PEMDAS
P = Parentheses
E = Exponent
M = Multiplication
A = Addition
S = Substractions
"""
# Example 1
''' ass pemda rule first will do multiplicatin and then addition '''
ex1 = 5 + 2 * 3

print(ex1)

''' We can change the pemdas order by using parenthesis'''

ex2 = (5 + 2) * 3
print(ex2)
num1 = 20
num2 = 30
print('\n')
print("Exmaple of Arthimatic Operation \n")
print('Num1 \tOp \tNum2 \tResult')
print('*' * 30)

# addition
print('{} \t+ \t{} \t={}'.format(num1, num2, num1+num2))
print('-' * 30)

# subtraction
print('{} \t- \t{} \t={}'.format(num2, num1, num2-num1))
print('-' * 30)
# multiplication
print('{} \t* \t{} \t={}'.format(num1, num2, num1*num2))
print('-' * 30)
# division
print('{} \t/ \t{}  \t= {}'.format(num2, num1, num2/num1))
print('-' * 30, '\n')
print("Example of Logical Operator \n")
a = True
b = False
print('value \tisTrue \tisFasle')
print('*' * 25)
print('{} \t{} \t{}'.format(a, a, not a))
print('-' * 25)
