import json
import ui

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


    with open ("data.json", 'w', encoding = 'utf-8') as write_file:
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
    
    with open ("data.json", 'r', encoding = 'utf-8') as f:

        new_data = json.load(f)
        # print (data)
        # listobj.append(dic)
    new_data.append(dic)
    
    with open ("data.json", 'w', encoding = 'utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)