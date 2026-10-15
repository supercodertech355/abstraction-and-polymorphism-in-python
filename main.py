from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
       print("I can walk and run")

class snake(animal):
    def move(self):
       print("I can slither")


R = human()
R.move()

K = snake()
K.move()