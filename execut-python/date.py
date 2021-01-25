import datetime

print(datetime.date.today())

current_time = datetime.datetime.now().time()
print(current_time)

clock = current_time.strftime("%I : %M : %S %p")
print(clock)
