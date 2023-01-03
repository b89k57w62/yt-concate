from step import Step


class ReadCaption(Step):
    def Process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exist(yt):
                continue
        
            captions = {}  #  key is caption , value is time
            with open((yt.get_caption_path), 'r') as f:
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
            
            yt.captions = captions
        return data                


