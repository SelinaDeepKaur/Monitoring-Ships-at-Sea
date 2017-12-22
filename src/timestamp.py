from datetime import datetime, timedelta
import time

t = 1326920388
dt = datetime.fromtimestamp(t) + timedelta(days=14)
print(int(time.mktime(dt.timetuple())))
