import json
import ui

str1 = "id, title, topic, date"                     # Сделать более универсально
keys = str1.split(", ")
str2 = str(ui.create()).split(" | ")
values = str2
dic = {}
dic = dict(zip(keys, values))
# print (dic)
listobj=[]
listobj.append(dic)
print(listobj)

# with open ("data.json", encoding = 'utf-8') as f:
#     listobj = json.load(f)
#     print (listobj)
#     print (type(listobj))
#     # listobj.append(dic)
#     listobj.update

# with open ("data.json", 'w', encoding = 'utf-8') as write_file:
#     json.dump (listobj, write_file, ensure_ascii=False, indent=2)