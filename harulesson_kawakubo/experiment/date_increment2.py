from datetime import datetime, timedelta


def create_range_date(dlist):   
    for i in range(15):
        print(dlist[i % len(dlist)])
        dlist[i % len(dlist)] += timedelta(weeks=1)
        i += 1

if __name__ == "__main__":
    # 週2日の場合の指定
    dt1 = datetime(2024, 1, 30, 18, 0)
    dt2 = datetime(2024, 2, 2, 19, 0)
    dlist = [dt1, dt2]
    create_range_date(dlist)

