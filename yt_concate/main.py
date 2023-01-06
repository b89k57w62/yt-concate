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


CHANNEL_ID = 'UCt_NLJ4McJlCyYM-dSPRo7Q'
def main():
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

    inputs = {        
        'channel_id' : CHANNEL_ID ,
        'serch_word' : 'incredible' ,
        'limit' : 25 ,

        }
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
    


