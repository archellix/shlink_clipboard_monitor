import logging, logging.config

from bestconfig import Config

config = Config()
logging.config.dictConfig(config['logging'])

def getLogger(name):
    logger = logging.getLogger(name)
    return logger