import sys
from datetime import datetime, timedelta

start = datetime.strptime(input().strip(), "%d.%m.%Y")
tasks = {}

for line in sys.stdin:
    data = line.strip().split()
    if not data:
        break
    task, total, a = data
    tasks[task] = (int(total), int(a))

wekkks = {"washing": 0, "ironing": 2, "cleaning": 3}
cur = start

while any(total > 0 for total, _ in tasks.values()):
    for task, (total, a) in tasks.items():
        if total > 0 and cur.weekday() == wekkks.get(task, None):
            perform = min(total, a)
            total -= perform
            print(cur.strftime("%d.%m.%Y"), task, perform)
            tasks[task] = (total, a)
    cur += timedelta(days=1)
