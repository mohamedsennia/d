import datetime
today = datetime.datetime.now()
a=1
for i in range(2000000):
    a=2
later = datetime.datetime.now()
diff=later-today
print(diff.total_seconds())