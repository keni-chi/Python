from abc import ABC, abstractmethod
from log_util import LogUtil
import datetime
import logging

logger = LogUtil.setup_logger('./log/{0}.log'.format(datetime.date.today()))
logger.setLevel(logging.INFO)  # INFO, DEBUG

class BaseService(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def preprocessing(self):
        pass

    @abstractmethod
    def main_processing(self):
        pass

    def execute(self):
        logger.info('execute---------start')
        try:
            self.get_data()
            self.preprocessing()
            self.main_processing()
            x = {'k': 'v'}
            y = x['k1']
        except Exception as e:
            print(e)
            logger.exception(f'CODE001: {e}')

        logger.info('execute---------end')
