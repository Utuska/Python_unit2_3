month = input("Введите месяц:")
if month:
    date = int(input("Введите дату"))
    if 1 <= date <= 31:
        if 22 <= date <= 31 and month.lower() == 'декабрь':
            print("Козерог")
        elif 1 <= date <= 19 and month.lower() == 'январь':
            print("Козерог")
        elif 22 <= date <= 31 and month.lower() == 'январь':
            print("Водолей")
        elif 1 <= date <= 18 and month.lower() == 'февраль':
            print("Водолей")
        elif 19 <= date <= 31 and month.lower() == 'февраль':
            print("Рыбы")
        elif 1 <= date <= 20 and month.lower() == 'март':
            print("Рыбы")
        elif 21 <= date <= 31 and month.lower() == 'март':
            print("Овен")
        elif 1 <= date <= 20 and month.lower() == 'апрель':
            print("Овен")
        elif 21 <= date <= 31 and month.lower() == 'апрель':
            print("Телец")
        elif 1 <= date <= 20 and month.lower() == 'май':
            print("Телец")
        elif 21 <= date <= 31 and month.lower() == 'май':
            print("Близнецы")
        elif 1 <= date <= 20 and month.lower() == 'июнь':
            print("Близнецы")
        elif 21 <= date <= 31 and month.lower() == 'июнь':
            print("Рак")
        elif 1 <= date <= 22 and month.lower() == 'июль':
            print("Рак")
        elif 23 <= date <= 31 and month.lower() == 'июль':
            print("Лев")
        elif 1 <= date <= 22 and month.lower() == 'август':
            print("Лев")
        elif 23 <= date <= 31 and month.lower() == 'август':
            print("Дева")
        elif 1 <= date <= 23 and month.lower() == 'сентябрь':
            print("Дева")
        elif 24 <= date <= 31 and month.lower() == 'сентябрь':
            print("Весы")
        elif 1 <= date <= 23 and month.lower() == 'октябрь':
            print("Весы")
        elif 24 <= date <= 31 and month.lower() == 'октябрь':
            print("Скорпион")
        elif 1 <= date <= 21 and month.lower() == 'ноябрь':
            print("Скорпион")
        elif 22 <= date <= 31 and month.lower() == 'ноябрь':
            print("Стрелец")
        elif 1 <= date <= 21 and month.lower() == 'декабрь':
            print("Стрелей")
        else:
            print("Неверная дата или месяц")