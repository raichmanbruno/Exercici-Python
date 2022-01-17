# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:20:25 2022

@author: Bruno
"""

from ApiService import ApiService


class App:
    def __init__(self):
        self._api_service = ApiService()

    def api_service(self) -> ApiService:
        return self._api_service