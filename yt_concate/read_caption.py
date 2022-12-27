import os
from pprint import pprint

from step import Step
from setting import Captions_Dir

class ReadCaption(Step):
    def Process(self, data, inputs, utils):
        data = {}  #  key is Caption_file_name , value is captions_dic
        for caption_file in os.listdir(Captions_Dir):
            captions = {}  #  key is caption , value is time
            with open(os.path.join(Captions_Dir, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            pprint(data)
            data[caption_file] = captions
        return data                


