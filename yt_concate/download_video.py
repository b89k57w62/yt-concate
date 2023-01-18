import os
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
            if int(len([name for name in os.listdir(Videos_Dir) if os.path.isfile(os.path.join(Videos_Dir, name))])) > inputs['limit']:
                print('the numbers of videos are up to 25!!!')
                break
            else:

                print('downloading', url)
                YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path= Videos_Dir, filename= yt.id + '.mp4')
            

        return data    

