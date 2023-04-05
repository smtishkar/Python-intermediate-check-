import json
import ui
from os import path
# import os
# print(os.path.abspath("data.json"))

filename = 'd:/GeekBrains/Intermediate check/1. Notepad/data.json' 

# if path.isfile(filename) is False:
#     raise Exception ("File not found") 

def create_note():
    str1 = "id, title, topic, date"                     # Сделать более универсально
    keys = str1.split(", ")
    str2 = str(ui.create()).split(" | ")
    values = str2
    dic = {}
    dic = dict(zip(keys, values))
    listobj=[]
    listobj.append(dic)

    # with open ("data.json", 'w', encoding = 'utf-8') as f:
    #     listobj = json.load(f)
    #     # print (data)
    #     # listobj.append(dic)
    #     listobj.update(dic)
    #     json.dump(listobj, f)


    with open (filename, 'w', encoding = 'utf-8') as write_file:
        json.dump (listobj, write_file, ensure_ascii=False, indent=2)


    # with open ("data.json", 'w', encoding = 'utf-8') as write_file:
    #     json.dump (dic, write_file, ensure_ascii=False, indent=2)
 
def create_note_second():
    str1 = "id, title, topic, date"                     # Сделать более универсально
    keys = str1.split(", ")
    str2 = str(ui.create()).split(" | ")
    values = str2
    dic = {}
    dic = dict(zip(keys, values))
    
    with open (filename, 'r', encoding = 'utf-8') as f:
        new_data = json.load(f)

    new_data.append(dic)
    
    with open (filename, 'w', encoding = 'utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

def show_all():
    with open (filename, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
        for i in new_data:
            print (i)

def find_note(id):
    with open (filename, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
        for i in new_data:
            for key, value in i.items():
                if value == id:
                    print (i)


def find_and_delete(id):
    with open (filename, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
        for i in range(len(new_data)):
            if new_data[i]['id'] == id:
                del new_data[i]
                break
       
    with open (filename, 'w', encoding = 'utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

def correct_not(id,new_topic,date):
    with open (filename, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
        for i in range(len(new_data)):
            if new_data[i]['id'] == id:
                # new_topic = input ("Введите новый текст: ")
                new_data[i]["topic"] = new_topic
                new_data[i]["date"] = date
                break
       
    with open (filename, 'w', encoding = 'utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
