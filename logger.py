import json
import ui

def create_note():
    str1 = "id, title, topic, date"                     # Сделать более универсально
    keys = str1.split(", ")
    str2 = str(ui.create()).split(" | ")
    values = str2
    dic = {}
    dic = dict(zip(keys, values))
    # print(dic)


    # data = {11111111111:"ewew"}
    # data = {title: }
    with open ("data.json", 'w') as write_file:
        json.dump (dic, write_file)