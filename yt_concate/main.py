from get_video_list import GetVideoList
from download_captions import DownloadCaption
from step import StepException
from pipeline import Pipeline

from utils import Utils
from preflight import Preflight
CHANNEL_ID = 'UCt_NLJ4McJlCyYM-dSPRo7Q'
def main():
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaption(),

    ]

    inputs = {        
        'channel_id' : CHANNEL_ID
        }
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
    


