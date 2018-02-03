import logging
from logging.handlers import SysLogHandler

class SysLogger:
    
    # This class is used to log to a file for now for testing. Later on a syslog handler should be added (the file handler can still be used for logging locally as well).
    
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' # default log format (improvement to be made: prettier formatting)
    log_level = 'INFO' # Default log level
    log_filename = 'logs.txt' # Log file for testing
   
    def __init__(self, facility, format=log_format, level=log_level, filename=log_filename):
        """
        Mandatory params:
            facility: the facility name
            
        Optional params:
            format: log format to be used (the following document can be referenced for this: https://docs.python.org/3/library/logging.html#logrecord-attributes)
            level: if desired, the log level can be specified (DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET)
            filename: different file for logging
        """
        
        # initial logger config
        self.logger = logging.getLogger(facility)
        
        # set the logging format
        self.formatter = logging.Formatter(format)
        
        # set log level
        self.logger.setLevel(level)
        
        # create the default handler (a file handler in this case)
        self.handler = logging.FileHandler(filename)
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
    
    
    def set_log_level(self, level):
        self.logger.setLevel(level)
    
    # The methods below are for logging the messages with the desired level
    def debug(self, message):
        self.logger.debug(message)
        
    def info(self, message):
        self.logger.info(message)
        
    def warning(self, message):
        self.logger.warning(message)
        
    def error(self, message):
        self.logger.error(message)
        
    def critical(self, message):
        self.logger.critical(message)
  
# code blow is for testing (when executing this file directly)     
if __name__ == '__main__':
    
    # Create logger object with the default log level(INFO)
    logger = SysLogger(facility=__name__)
    
    # Only INFO, WARNING, ERROR, and CRITICAL should get logged:
    logger.debug('debug test')
    logger.info('info test')
    logger.warning('warning test')
    logger.error('error test')
    logger.critical('critical test')
    
    # Change log level to DEBUG
    logger.set_log_level('DEBUG')
    
    # This should get logged now
    logger.debug('debug test')
 
