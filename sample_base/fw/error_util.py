# -*- coding: utf-8 -*-


class AppException(Exception):
    def __init__(self, message):
        super().__init__(message)
