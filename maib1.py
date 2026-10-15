from abc import ABC, abstractmethod

class absclass(ABC):

    def print(self,x):
        print("passed value", x)

    @abstractmethod
    def task(self):
        print("We are inside absclass task ")


class test_class(absclass):
    def task(self):
        print("We are inside test class")


o = test_class()
o.task()
o.print(5)