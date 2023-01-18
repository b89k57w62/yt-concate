import os

from step import Step
from pytube import YouTube

from setting import Captions_Dir
from utils import Utils
class DownloadCaption(Step):
    def Process(self, data, inputs, utils):
        for yt in data:
            print('downloding caption for', yt.id)
            if utils.caption_file_exist(yt):
                print('Found exist caption file.')
                continue
            if int(len([name for name in os.listdir(Captions_Dir) if os.path.isfile(os.path.join(Captions_Dir, name))])) > inputs['limit']:
                print('the numbers of videos are up to 25!!!')
                break
            try:

                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt =(en_caption.generate_srt_captions())
            except AttributeError:
                    print('AttributeError when downloading caption', yt.url)
                    continue
            text_file = open(yt.get_caption_path, "w", encoding= 'utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data    
            



