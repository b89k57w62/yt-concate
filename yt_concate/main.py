import sys 
import getopt
sys.path.append('../')
sys.path.append('/Users/mac/Desktop/yt-concate/yt-venv/lib//site-packages')
from step import StepException
from pipeline import Pipeline
from utils import Utils
from preflight import Preflight
from get_video_list import GetVideoList
from initializeyt import InitializeYT
from download_captions import DownloadCaption
from read_caption import ReadCaption
from serch import Serch
from download_video import DownloadVideo
from edit_video import EditVideo
from postflight import Postflight



def main():
    

    inputs = {        
        'channel_id' : 'UCt_NLJ4McJlCyYM-dSPRo7Q' ,
        'serch_word' : 'incredible' ,
        'limit' : 25 ,
        'cleanup': False
        }    
    
    utils = Utils()
    if utils.output_file_exist(inputs['channel_id'], inputs['serch_word']):
        ans = input('clips video already exists for the channel and key word \n still want to preceed?(Y/N)')            
        if ans.upper() == 'Y':
            process_req(inputs, utils)
        else:                
            print('exiting program...')
            return
    else:
        process_req(inputs, utils)            

    

def process_req(inputs, utils):
    steps = [
        Preflight() ,
        GetVideoList() ,
        InitializeYT() ,
        DownloadCaption() ,
        ReadCaption() ,
        Serch() , 
        DownloadVideo(),
        EditVideo(),
        Postflight(),
        
    ]
    p = Pipeline(steps)
    p.run(inputs, utils)



if __name__ == '__main__':
    main()
    


