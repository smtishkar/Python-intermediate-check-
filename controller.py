import ui
import model
from os import path


def run():
    user_request = ui.choose_action()
    if user_request == 1:
        if path.isfile(model.filename) is False:
            model.create_note()
        else: 
            model.create_note_second() 
    if user_request == 2:
        model.show_all()
    if user_request == 3:
        id = ui.find_note()
        model.find_note(id)
    if user_request ==4:
        id=ui.find_note()
        topic=ui.topic_correction()
        date = ui.time_correction()
        model.correct_note(id,topic,date)
    if user_request ==5:
        id = ui.find_note()
        model.find_and_delete(id)
    