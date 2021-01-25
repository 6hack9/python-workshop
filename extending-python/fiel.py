# Creating File
import time
from datetime import datetime
with open('../fiels/create.tx', 'w') as c:
    c.write('hello world\n')

# Reading file
with open('../fiels/pg37431.txt', mode='r') as target:
    content = target.read()
# print(content)


f = open('../fiels/log.txt', 'w')


for i in range(0, 10):
    print(datetime.now().strftime('%Y-%m-%d %H:%M :%S'))
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
    f.write(str(i))
    f.write('\n')

f.close()
