import os

from step import Step
from pytube import YouTube

from setting import Captions_Dir
from utils import Utils
class DownloadCaption(Step):
    def Process(self, data, inputs, utils):
        for url in data:
            print('downloding caption for', url)
            if utils.caption_file_exist(url):
                print('Found exist caption file.')
                continue
            try:

                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt =(en_caption.generate_srt_captions())
            except AttributeError:
                    print('AttributeError when downloading caption', url)
                    continue
            text_file = open(utils.get_caption_path(url), "w", encoding= 'utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            



