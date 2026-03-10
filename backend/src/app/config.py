
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    # pydantic-settings
    # attribute name is the default env-variable name
    # the initialized value is the default value

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    # API
    API_DEBUGMODE: bool = True
    API_DOCS: bool = False
    API_LOGFILE: str = "./api.log"
    API_PORT: int = 8000
    API_HOST: str = '0.0.0.0'

    # CORS
    CORS_ORIGINS: str = '*'
    CORS_METHODS: str = '*'











import logging
class CustomFormatter(logging.Formatter):
    # more info: https://en.wikipedia.org/wiki/ANSI_escape_code
    # bold = 1

    reset = "\033[0m"

    bold_white = "\033[97;1m"
    bold_red = "\033[31;1;40m"

    black = "\033[30;40m"
    red = "\033[31;40m"
    green = "\033[32;40m"
    yellow = "\033[33;40m"
    blue = "\033[34;40m"
    magenta = "\033[35;40m"
    cyan = "\033[36;40m"
    lightgray = "\033[37;40m"
    gray = "\033[90;40m"
    brightred = "\033[91;40m"
    brightgreen = "\033[92;40m"
    brightyellow = "\033[93;40m"
    darkblue = "\033[94;40m"
    pink = "\033[95;40m"
    lightblue = "\033[96;40m"
    white = "\033[97;40m"

    format = "%(asctime)s %(levelname)s | %(module)s : %(message)s"

    FORMATS = {
        logging.DEBUG: lightgray+"%(asctime)s - %(name)s - "+gray+"%(levelname)s"+lightgray+" | "+bold_white+"%(module)s"+reset+lightgray+" : %(message)s "+gray+"(%(filename)s:%(lineno)d)"+reset,
        logging.INFO: lightgray+"%(asctime)s - %(name)s - "+green+"%(levelname)s"+lightgray+" | "+bold_white+"%(module)s"+reset+lightgray+" : %(message)s "+gray+"(%(filename)s:%(lineno)d)"+reset,
        logging.WARNING: lightgray+"%(asctime)s - %(name)s - "+yellow+"%(levelname)s"+lightgray+" | "+bold_white+"%(module)s"+reset+lightgray+" : %(message)s "+gray+"(%(filename)s:%(lineno)d)"+reset,
        logging.ERROR: lightgray+"%(asctime)s - %(name)s - "+red+"%(levelname)s"+lightgray+" | "+bold_white+"%(module)s"+reset+lightgray+" : %(message)s "+gray+"(%(filename)s:%(lineno)d)"+reset,
        logging.CRITICAL: lightgray+"%(asctime)s - %(name)s - "+bold_red+"%(levelname)s"+lightgray+" | "+bold_white+"%(module)s"+reset+lightgray+" : %(message)s "+gray+"(%(filename)s:%(lineno)d)"+reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class NoTraceFilter(logging.Filter):
    def filter(self, record):
        return "_trace" in record.getMessage()

from typing import Tuple
def getLoggingSetup(debugmode: bool = True, logfile: str = None) -> Tuple[dict, int]:
    """
    returns the generated dict for use in dictConfig and the loglevel
    """

    loglevel = logging.INFO
    if debugmode:
        loglevel = logging.DEBUG
    handlers: list = ["console"]
    if logfile != None:
        if os.path.exists(logfile):
            open(logfile, 'w').close()
        handlers.append("file")

    config = {
        "version": 1,
        "encoding": "utf-8",
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": CustomFormatter,
                "datefmt": "%B %d, %Y %H:%M:%S"
            },
            "colorless": {
                "format": "%(asctime)s - %(name)s - %(levelname)s | %(module)s : %(message)s (%(filename)s:%(lineno)d)",
                "datefmt": "%B %d, %Y %H:%M:%S"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                #"filters": ["no_trace_filter"]
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": logfile,
                "formatter": "colorless"
            }
        },
        "filters": {
            "no_trace_filter": {
                "()": NoTraceFilter, 
            }, 
        },
        "root": {"level": logging.getLevelName(loglevel), "handlers": handlers}
    }

    return config, loglevel
