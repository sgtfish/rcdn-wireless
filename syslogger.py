import logging
from logging.handlers import SysLogHandler
import pdb

handler = logging.FileHandler('log.txt')
handler2 = SysLogHandler(address=("10.154.66.159", 514))

def setup(facility):
    global handler
    global handler2

    logger = logging.getLogger(facility)
    logger.setLevel(logging.DEBUG)

    #handler = logging.FileHandler('log.txt')

    formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
    formatter2 = logging.Formatter('[%(name)s] - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    handler2.setFormatter(formatter2)

    logger.addHandler(handler)
    logger.addHandler(handler2)

    return logger

def log(facility, level, message):
    global handler
    """global a
    if a == True:
        logger = setup(facility)
        a = False
    #print(logger)
    """
    logger = setup(facility)

    if level == 'DEBUG':
        #print('logging debug...')
        logger.debug(message)

    elif level == 'INFO':
        #print('logging info...')
        logger.info(message)

    elif level == 'WARNING':
        #print('logging warning...')
        logger.warn(message)

    elif level == 'ERROR':
        #print('logging error...')
        logger.error(message)

    elif level == 'CRITICAL':
        #print('logging critical...')
        logger.critical(message)
    #logger.removeHandler(handler)
