import os


from setting import Captions_Dir
from setting import Videos_Dir

class YT:
    def __init__(self, url):
        self.url = url 
        self.id = self.get_video_id_from_url(self.url)
        self.get_caption_path = self.get_caption_path()
        self.get_video_path = self.get_video_path()
        self.captions = None
    
    def __str__(self):
        return '<YT(' + str(self.id) +')>'

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]
    def get_caption_path(self):
        return os.path.join(Captions_Dir, self.id +'.txt')
    def get_video_path(self):
        return os.path.join(Videos_Dir, self.id +'.mp4')
    
