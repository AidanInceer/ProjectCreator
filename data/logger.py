import logging

from colorama import Fore


class CustomFormatter(logging.Formatter):
    blue = Fore.LIGHTBLUE_EX
    white = Fore.WHITE
    yellow = Fore.YELLOW
    light_red = Fore.LIGHTRED_EX
    red = Fore.RED
    reset = Fore.RESET
    format = "[%(asctime)s][%(levelname)s][%(module)s][%(lineno)d]: %(message)s"

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: white + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: light_red + format + reset,
        logging.CRITICAL: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)
