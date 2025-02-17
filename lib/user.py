#!/usr/bin/env python

class User:
    #first_name and last_name attributes
    def __init__(self, first_name, last_name, knowledge=''):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge

        