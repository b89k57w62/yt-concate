from get_video_list import GetVideoList
from step import StepException
from pipeline import Pipeline
CHANNEL_ID = 'UCt_NLJ4McJlCyYM-dSPRo7Q'
def main():
    steps = [
        GetVideoList(),
    ]

    inputs = {        
        'channel_id' : CHANNEL_ID
        }
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
    

