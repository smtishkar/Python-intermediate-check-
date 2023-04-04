import uuid
import datetime

def choose_action():
    print (f"Выберите действие: \nСоздать заметку - 1\nСписок заметок - 2\n"
                "Редактировать заметку - 3\nУдалить заметку - 4\n")
    request = int(input("Введите значение: "))
    return request


def create():
    id = str(uuid.uuid4()).split('-')[0]
    title = input ("Введите название заметки: ")
    topic = input ("Введите заметку: ")
    date = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    # return (id,title,topic,date)
    return f'{id} | {title} | {topic} | {date}'

def see_all():
    pass

def correct():
    pass

def delete():
    pass