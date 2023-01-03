from step import Step
from found import Found


class Serch(Step):
    def Process(self, data, inputs, utils):
        serch_word = inputs['serch_word']
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if serch_word in caption:   
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        print(len(found))
        return found            

                



