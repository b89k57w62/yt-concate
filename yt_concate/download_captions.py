import os

from step import Step
from pytube import YouTube

from setting import Captions_Dir
from utils import Utils
class DownloadCaption(Step):
    def Process(self, data, inputs, utils):
        for url in data:
            source = YouTube(url)


            en_caption = source.captions.get_by_language_code('a.en')

            en_caption_convert_to_srt =(en_caption.generate_srt_captions())

            print(en_caption_convert_to_srt)
            #save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break



