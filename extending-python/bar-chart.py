import matplotlib.pyplot as plt

grades = ['A', 'B', 'C', 'D', 'E', 'F']
students_count = [20, 30, 10, 5, 8, 2]
plt.title('Student Grade System')
plt.ylabel('Student Number')
plt.xlabel('Grades')
plt.bar(grades, students_count, color=['green', 'gray'])

plt.show()
