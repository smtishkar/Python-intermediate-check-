import uuid
import datetime

def choose_action():
    print (f"Выберите действие: \nСоздать заметку - 1\nСписок заметок - 2\n"
                "Поиск заметки - 3\nРедактировать заметку - 4\nУдалить заметку - 5\n")
    valid = False
    while not valid:
        request = input("Введите значение: ")
        try:
            request = int(request)
            if request <5 and request > 0:
                valid = True
            else:
                print("Не корректный ввод, повторите попытку")
        except:
            print("Не корректный ввод, повторите попытку")
            continue
    return request

def create():
    id = str(uuid.uuid4()).split('-')[0]
    title = input ("Введите название заметки: ")
    topic = input ("Введите заметку: ")
    date = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    return f'{id} | {title} | {topic} | {date}'

def find_note():
    id_for_find = input("Введите ID нужной заметки: ")
    return id_for_find

def topic_correction():
    new_topic = input ("Введите новый текст: ")
    return new_topic

def time_correction():
    new_date = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    return new_date