
from step import Step
class Preflight(Step):
    def Process(self, data, inputs, utils):
        utils.create_dir()