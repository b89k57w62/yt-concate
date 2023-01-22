import os
import shutil

from setting import Captions_Dir
from setting import Downloads_Dir
from setting import Videos_Dir
from setting import Outputs_Dir
class Utils:
    def __init__(self):
        pass
    
    def create_dir(self):
        os.makedirs(Downloads_Dir, exist_ok= True)
        os.makedirs(Captions_Dir, exist_ok= True)
        os.makedirs(Videos_Dir, exist_ok= True)
        os.makedirs(Outputs_Dir, exist_ok= True)
    
    def delete_file(self, channel_id):
        shutil.rmtree(Captions_Dir)
        shutil.rmtree(Videos_Dir)
        os.remove(self.get_video_list_filepath(channel_id))
    
    

    def caption_file_exist(self, yt):
        path = yt.get_caption_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    def video_file_exist(self, yt):
        path = yt.get_video_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(Downloads_Dir, channel_id +'.txt')        


    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def output_filepath(self, channel_id, serch_word):
        output_filename = channel_id + '_' + serch_word + '.mp4'
        return os.path.join(Outputs_Dir, output_filename)

    def output_file_exist(self, channel_id, serch_word):
        path = self.output_filepath(channel_id, serch_word)
        return os.path.exists(path) and os.path.getsize(path) > 0

        
