from step import Step
from yt import YT

class InitializeYT(Step):
    def Process(self, data, inputs, utils):
        return [YT(url) for url in data]   # tranform url to YT objects
