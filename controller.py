import ui
import logger
from os import path


def run():
    user_request = ui.choose_action()
    if user_request == 1:
        if path.isfile(logger.filename) is False:
        # ui.create()
        # print(ui.create())
            logger.create_note()
        else: 
           logger.create_note_second() 
    # if user_request == 2:
    #     logger.create_note_second()




        # str1 = "id, title, topic, date"
        # keys = str1.split(", ")
        # str2 = str(ui.create()).split(" | ")
        # values = str2
        # dic = {}
        # dic = dict(zip(keys, values))
        # print(dic)
