import os


from setting import Captions_Dir
from setting import Downloads_Dir
from setting import Videos_Dir

class Utils:
    def __init__(self):
        pass
    
    def create_dir(self):
        os.makedirs(Downloads_Dir, exist_ok= True)
        os.makedirs(Captions_Dir, exist_ok= True)
        os.makedirs(Videos_Dir, exist_ok= True)
    
    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]
    
    def get_caption_path(self, url):
        return os.path.join(Captions_Dir, self.get_video_id_from_url(url) +'.txt')
        
