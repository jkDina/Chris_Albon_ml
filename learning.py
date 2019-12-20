from datetime import datetime, date
from datetime import timedelta
import dbm
import json

#T = 2 * t + 1

variant = input("""Выберите действие:
1.Ввод новых данных
2.Просмотр плана дня
3.Просмотр плана дней выбранного задания
4.Выход
""")

with dbm.open("reminders", "c") as storage:
    variant = int(variant)
    if variant == 1:
        today = date.today()
        task = input('Введите текст задания для повторения\n')
        #format_today = today.strftime('%Y-%m-%d')

        date_list = []
        days = [1, 2, 5, 11, 23, 47, 95, 191]
        print(f'Следующие дни для повторения темы {task}:')
        
        for day in days:
            d = today + timedelta(day)
            print(d)
            date_list.append(d)

        
        format_days = []
        for day in date_list:
            format_day = day.strftime('%Y-%m-%d')
            format_days.append(format_day)

        storage[task] = json.dumps(format_days)
        
        
    elif variant == 2:
        task_date = input('Введите интересующую Вас дату в формате "2012-09-20" для повторения уроков на эту дату\n')
        tasks = []
        for key in storage.keys():
            dates = json.loads(storage[key].decode('utf-8'))
            if task_date in dates:
                tasks.append(key.decode('utf-8'))
                
        print(f'На дату {task_date} у Вас следующие уроки для повторения')
        for task in tasks:
            print(task)
    elif variant == 3:
        task = input('Введите задание для просмотра дней его повторения\n')
        dates = storage.get(task)
        if dates is None:
            print('Задание не обнаружено')
        else:
            dates = json.loads(dates)
            for d in dates:
                print(d)
    elif variant == 4:
        pass
