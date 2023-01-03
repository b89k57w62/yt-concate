from pytube import YouTube

from step import Step
from setting import Videos_Dir
class DownloadVideo(Step):
    def Process(self, data, inputs, utils):
        
        yt_set = set([found.yt for found in data])
        
        for yt in yt_set:
            url = yt.url
            
            if utils.video_file_exist(yt):
                print(f'found existing video file {url} , skip')
                continue
            
            print('downloading', url)
            YouTube(url).streams.first().download(output_path= Videos_Dir, filename= yt.id + '.mp4')

        return data    

