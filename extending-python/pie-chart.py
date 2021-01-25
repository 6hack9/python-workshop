import matplotlib.pyplot as plt
labels = ['Monica', 'Adrian', 'Jared']
num = [230, 100, 98]  # Note that this does not need to be percentages
plt.title('Votting Results: Club President', fontdict={'fontsize': 20})

plt.pie(num, labels=labels, colors=[
        'lightblue', 'lightgreen', 'yellow'], autopct='%1.1f%%')

plt.show()
