# -*- coding: utf-8 -*-
from logging import getLogger, StreamHandler, Formatter, FileHandler, DEBUG

class LogUtil:
    def __init__(self):
        pass

    @classmethod
    def setup_logger(cls, log_folder, modname=__name__):
        logger = getLogger(modname)
        logger.setLevel(DEBUG)

        sh = StreamHandler()
        sh.setLevel(DEBUG)
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh.setFormatter(formatter)
        logger.addHandler(sh)

        fh = FileHandler(log_folder, encoding='utf-8')
        fh.setLevel(DEBUG)
        fh_formatter = Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s')
        # fh_formatter = Formatter('%(asctime)s - %(filename)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)

        return logger
