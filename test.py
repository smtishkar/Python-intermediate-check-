import json
import ui
import os

# str1 = "id, title, topic, date"                     # Сделать более универсально
# keys = str1.split(", ")
# str2 = str(ui.create()).split(" | ")
# values = str2
# dic = {}
# dic = dict(zip(keys, values))
# # print (dic)
# listobj=[]
# listobj.append(dic)
# print(listobj)

# with open ("data.json", encoding = 'utf-8') as f:
#     listobj = json.load(f)
#     print (listobj)
#     print (type(listobj))
#     # listobj.append(dic)
#     listobj.update

# with open ("data.json", 'w', encoding = 'utf-8') as write_file:
#     json.dump (listobj, write_file, ensure_ascii=False, indent=2)


# print(os.path.abspath("data.json"))


list = ['4', '2', '3']

numb = '4'

# def delete(number):



for i in range (len(list)):
    print (i)
    if list[i] == numb:
        index = i
        print(list[i])
list.pop(index)
print(list)



