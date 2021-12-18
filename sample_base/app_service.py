from fw.base_service import BaseService


class AppService(BaseService):
    def __init__(self):
        pass

    def get_data(self):
        print('AppService_get_data---------start')

    def preprocessing(self):
        print('AppService_preprocessing---------start')

    def main_processing(self):
        print('AppService_main_processing---------start')
