from datetime import datetime, timedelta

dt1 = datetime(2024, 1, 30, 18, 0)
dt2 = datetime(2024, 2, 2, 19, 0)
dlist = [dt1, dt2]

def create_range_date(dlist):   
    for i in range(15):
        print(dlist[i % len(dlist)])
        dlist[i % len(dlist)] += timedelta(weeks=1)
        i += 1

create_range_date(dlist)

