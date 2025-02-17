#!/usr/bin/env python

from user import User

#inherits from user class
class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # self.knowledge that points to an empty list
        self.knowledge = []
   
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge) # add knowledge to the knowledge list