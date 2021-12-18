# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class BaseService(ABC):

    def __init__(self, logger):
        self.logger = logger

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
        self.logger.info('execute---------start')
        try:
            self.get_data()
            self.preprocessing()
            self.main_processing()
            self.logger.info('execute---------end')
        except Exception as e:
            self.logger.exception(f'CODE001: {e}')
            
