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