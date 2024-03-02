from datetime import date, timedelta

# 1週間に2回授業する場合
# lesson_start_dates = [date(2024, 2, 21), date(2024, 2, 23)]
def create_dates(lesson_start_dates, times=15):
    datelist = []
    for i in range(times):
        datelist.append(lesson_start_dates[i % len(lesson_start_dates)])
        lesson_start_dates[i % len(lesson_start_dates)] += timedelta(weeks=1) 
    return datelist


if __name__ == "__main__":
    lesson_start_dates = [date(2024, 2, 21), date(2024, 2, 23)]
    datelist = create_dates(lesson_start_dates)
    for d in datelist:
        print(d)