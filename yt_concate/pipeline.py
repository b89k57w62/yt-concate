from step import StepException
class Pipeline:
    def __init__(self, steps):
        self.steps = steps    #stpes = list
    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.Process(data, inputs, utils)
            except StepException as e :
                print('Exception Happened', e)
                break    