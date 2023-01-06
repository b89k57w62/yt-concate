import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

#print(API_KEY)

Downloads_Dir = 'downloads'
Captions_Dir = os.path.join(Downloads_Dir, 'captions')
Videos_Dir = os.path.join(Downloads_Dir, 'videos')
Outputs_Dir = 'outputs'
