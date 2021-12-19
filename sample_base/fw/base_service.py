# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class BaseService(ABC):

    def __init__(self, logger):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def preprocessing(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def execute(self):
        self.logger.info('execute---------start')
        try:
            # # keyエラーでfwエラーの動作確認時にコメントイン
            # x = {'k': 'v'}
            # y = x['a']

            self.init()
            self.preprocessing()
            self.run()

            self.logger.info('execute---------end')
        except Exception as e:
            self.logger.exception('[code:fw001] サンプルfwエラーのメッセージ')