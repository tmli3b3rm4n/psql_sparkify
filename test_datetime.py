from datetime import datetime, date
stamp = 1541903636796

d = datetime.fromtimestamp(int(stamp / 1000))
d = tuple(d.timetuple())
print(d[0: 7])
print(d[-1] > 5)