from abc import ABC , abstractmethod


class Step(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def Process(self, data, inputs):
        pass 


class StepException(Exception):
    pass

