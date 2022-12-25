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

    def caption_file_exist(self, url):
        path = self.get_caption_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(Downloads_Dir, channel_id +'.txt')

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0


        
