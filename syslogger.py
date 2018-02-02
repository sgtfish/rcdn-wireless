import logging
from logging.handlers import SysLogHandler

def setup(facility):

    logger = logging.getLogger(facility)
    logger.setLevel(logging.DEBUG)
    
    handler = logging.FileHandler('log.txt')
    
    formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
    
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    return logger
    
def log(facility, level, message):
    
    logger = setup(facility)
    print(logger)
    
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
        
        

    
