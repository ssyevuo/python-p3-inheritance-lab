#!/usr/bin/env python

from user import User

import random

#Teacher class inherits from the User class
class Teacher(User):
    # the knowledge list
    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # the knowledge list is stored in the self.knowledge list
        self.knowledge = Teacher.knowledge

    def teach(self):
        # returns random element from knowledge list
        return random.choice(self.knowledge)
        