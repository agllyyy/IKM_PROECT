# проверка на корректную запись о сотруднике
def correct_piece(piece):
    if len(piece) != 10:
        return False
    if not (piece[3].isdigit() and piece[4].isdigit() 
            and piece[5].isdigit() and piece[8].isdigit()):
            return False
    try:
        float(piece[9])
        return True
    except ValueError:
        return False

# добавление данных из файла в список словарей с инфой о сотрудниках  
def adding_csv(filename):
    try:
        file = open(filename, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Проверьте имя файла и его расположение.")
        return []
    
    if file == '':
        print(f"Файл '{filename}' пуст.")
        return []
    
    file = [line.split(',') for line in file.split('\n')]
    result = []
    for i in range(len(file)):
        person = file[i]
        # проверка количества аргументов
        if (len(person) != 10):
            print(f"В строке {i + 1} ожидается 10 аргументов, но было получено {len(person)}! Строка не была учтена!")
            continue

        else:
            if not correct_piece(person):
                print(f"Некорректные данные в строке {i + 1}! Строка не была учтена!")
                continue

            sotrudnik = {
                'фамилия' : person[0],
                'имя' : person[1],
                'отчество' : person[2],
                'год' : int(person[3]),
                'месяц' : int(person[4]),
                'число' : int(person[5]),
                'отдел' : person[6],
                'должность' : person[7],
                'оклад' : int(person[8]),
                'стаж' : float(person[9])
                }
            result.append(sotrudnik)
    return result

# сортировка слиянием по ключу 
def sort_sl_key(arr,key_func):
    if len(arr) < 2:
        return arr
    
    result = arr.copy()

    sr = len(arr)//2
    L = arr[:sr]
    R = arr[sr:]

    L = sort_sl_key(L,key_func); R = sort_sl_key(R,key_func)

    l = r = k = 0
    while l < len(L) and r < len(R):
        if key_func(L[l]) <= key_func(R[r]):
            result[k] = L[l]
            l += 1
        else:
            result[k] = R[r]
            r += 1
        k += 1

    while l < len(L):
        result[k] = L[l]
        k += 1
        l += 1
    while r < len(R):
        result[k] = R[r]
        k += 1
        r += 1

    return result



# ключ сортировки для Отчета 1: год (по убыванию) + стаж (по убыванию) + фамилия (по возрастанию)
def key_report_1(sotrudnik):
    return (-sotrudnik['год'], -sotrudnik['стаж'], sotrudnik['фамилия'])

# формирует Отчет 1
def report_1(sotrudniki):
    return sort_sl_key(sotrudniki, key_report_1)

# вывод Отчета 1
def print_report_1(sorted_sotrudniki):
    print(f'\n\tОТЧЕТ 1: все сотрудники')
    
    if not sorted_sotrudniki:
            print("Нет данных для отображения.")
            return
    
    print("-" * 110)
    print(f"{'ФИО':<30} {'Дата рождения':<15} {'Отдел':<20} {'Должность':<25} {'Оклад':>8} {'Стаж':>6}")
    print("-" * 110)

    for s in sorted_sotrudniki:
        fio = f"{s['фамилия']} {s['имя']} {s['отчество']}"
        dr = f"{s['год']}-{s['месяц']:02d}-{s['число']:02d}" # Формат даты: ГГГГ-ММ-ДД

        print(f"{fio:<30} {dr:<15} {s['отдел']:<20} {s['должность']:<25} {s['оклад']:>8} {s['стаж']:>6}")

               
     
# ключ сортировки для Отчета 2: оклад (по убыванию) + фамилия (по возрастанию)
def key_report_2(sotrudnik):
    return (-sotrudnik['оклад'], sotrudnik['фамилия'])

# формирует Отчет 2
def report_2(sotrudniki):
    return sort_sl_key(sotrudniki, key_report_2)

# фильтрует список сотрудников по заданному отделу
def filter_key_by_otdel(sotrudniki,otdel):
    rezult = []
    for i in sotrudniki:
        if i['отдел'] == otdel:
            rezult.append(i)
    return rezult

# вывод Отчета 2
def print_report_2(sorted_sotrudniki,otdel):
    print(f'\n\tОТЧЕТ 2: Сотрудники отдела "{otdel}"')
    
    if not sorted_sotrudniki:
            print("Нет данных для отображения.")
            return
    
    print("-" * 55)
    for s in sorted_sotrudniki:
        fio = f"{s['фамилия']} {s['имя']} {s['отчество']}"
        print(f"{fio:<30} -\tОклад: {s['оклад']}")



# ключ сортировки для Отчета 3: должность (по возрастанию) + фамилия(по возрастанию)
def key_report_3(sotrudnik):
    return (sotrudnik['должность'], sotrudnik['фамилия'])

# формирует Отчет 3
def report_3(sotrudniki):
    return sort_sl_key(sotrudniki, key_report_3)

# вычисляет средний оклад по всем сотрудникам
def medium_money(sotrudniki):
    if not sotrudniki:
        return 0
    Sum = []
    for i in sotrudniki:
        Sum.append(i['оклад'])
    return sum(Sum) / len(sotrudniki)

# фильтрует список сотрудников, у которых оклад выше среднего
def filter_key_medium_money(sotrudniki, medium_money):
    rezult = []
    for i in sotrudniki:
        if i['оклад'] > medium_money:
            rezult.append(i)
    return rezult

# вывод Отчета 3
def print_report_3(sorted_sotrudniki,med_money):
    print(f'\n\tОТЧЕТ 3: Сотрудники с окладом выше среднего')
    print(f"Средний оклад по предприятию: {int(med_money)} руб.")
    print("-" * 86)

    if not sorted_sotrudniki:
        print("Нет сотрудников с окладом выше среднего.")
        return
    for s in sorted_sotrudniki:
        fio = f"{s['фамилия']} {s['имя']} {s['отчество']}"
        print(f'{fio:<35} -\t', f" {s['должность']:<25}", f" - {s['оклад']:>10} руб.")





# вывод меню для выбора Отчёта
def show_menu():
    print('\n' + '=' * 50)
    print(f'\tПРОГРАММА: УЧЕТ СОТРУДНИКОВ')
    print('=' * 50)
    print(f'1. Отчёт 1: Все сотрудники',
          f'\n2. Отчёт 2: По отделу',
          f'\n3. Отчёт 3: Оклад выше среднего',
          f'\n0. Выход')
    print('-' * 50)

# формирует список уникальных отделов в алфавитном порядке
def total_otdelov(sotrudniki):
    otdely = set()
    for i in sotrudniki:
        otdely.add((i['отдел']))
    return sorted(otdely)

# выводит список отделов и запрашивает у пользователя выбор отдела для отчёта 2
def vibor_otdel(sotrudniki):
    otdely = total_otdelov(sotrudniki)
    if not otdely:
        print("Нет данных об отделах.")
        return
    print(f'\tДоступные отделы:')
    for i, otdel in enumerate(otdely,1):
        print(f'{i}. {otdel}')

    while True: # для повторного ввода
        try:
            num_otdela = int(input('\nВведите номер отдела: '))
            if 1 <= num_otdela <= len(otdely):
                return otdely[num_otdela - 1]
            print('Такого номера нет. Введите номер из списка.')
        except ValueError:
            print('Некорректный ввод. Введите число из списка.')

# обрабатывает действия пользователя в главном меню и выполняет соответствующий отчёт
def obrabotka_vibora(vibor,sotrudniki):
    match vibor:
        case '1':
            if not sotrudniki:
                print("Нет данных для отчёта.")
            print_report_1(report_1(sotrudniki))
            return True
        
        case '2':
            if not sotrudniki:
                print("Нет данных для отчёта.")
            otdel = vibor_otdel(sotrudniki)
            if otdel is not None:
                filter_sotrudniki = filter_key_by_otdel(sotrudniki,otdel)
                print_report_2(report_2(filter_sotrudniki),otdel)
            return True

        case '3':
            if not sotrudniki:
                print("Нет данных для отчёта.")
            else:
                med_money = medium_money(sotrudniki)
                filter_med_money_sotrudniki = filter_key_medium_money(sotrudniki,med_money)
                print_report_3(report_3(filter_med_money_sotrudniki),med_money)
            return True

        case '0':
            return False
        
        case _:
            print(f"\nНеверный выбор: '{vibor}'. Введите цифру 0–3.")
            return True

# главная функция программы
def zapusk_program(): 
    sotrudniki = adding_csv('working.csv')

    if not sotrudniki:
        print("Нет данных. Программа завершена.")
        return

    while True:
        show_menu()
        vibor = input('Введите цифру(0-3), чтобы выбрать действие: ').strip()
        if not obrabotka_vibora(vibor,sotrudniki):
            break
    print(f'\nПрограмма завершена.')


zapusk_program()
