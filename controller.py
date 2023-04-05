import ui
import logger
from os import path


def run():
    user_request = ui.choose_action()
    if user_request == 1:
        if path.isfile(logger.filename) is False:
            logger.create_note()
        else: 
           logger.create_note_second() 
    if user_request == 2:
        logger.show_all()
    if user_request == 3:
        id = ui.find_note()
        logger.find_note(id)
    if user_request ==4:
        id=ui.find_note()
        logger.correct_not(id)
    if user_request ==5:
        id = ui.find_note()
        logger.find_and_delete(id)
    