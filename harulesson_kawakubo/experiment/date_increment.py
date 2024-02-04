from datetime import datetime, timedelta

dt = datetime(2024, 1, 31, 18, 0)

for _ in range(15):
    print(dt)
    dt += timedelta(weeks=1)
    


