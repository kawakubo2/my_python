weekdays_ja = ["日","月","火","水","木","金","土"]
weendays_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

weekdays_dict = {ja: en for ja, en in zip(weekdays_ja, weendays_en)}
print(weekdays_dict)

weekdays_dict2 = {en: ja for ja, en in zip(weekdays_ja, weendays_en)}
print(weekdays_dict2)
