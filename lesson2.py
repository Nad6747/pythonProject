from datetime import datetime

data =datetime.now()
time = data.strftime("%H:%M:%S")
day = datetime.date(data)
day2 = datetime.weekday(data)
if day2 == 0:
    day2 ="Понедельник"
elif day2 == 1:
    day2 ="Вторник"
elif day2 == 2:
    day2 = ("Среда")
elif day2 == 3:
    day2 ="Четверг"
elif day2 == 4:
    day2 ="Пятница"
elif day2 == 5:
    day2 ="Суббота"
elif day2 == 6:
    day2 ="Воскресенье"

print(f"Сегодня у вас {day},что это {day2} и сейчас такое то время -{time}")


