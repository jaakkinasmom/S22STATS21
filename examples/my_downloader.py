import pytube
import validators
import requests

"""
my_downloader.py 03-21-2022
runs at the command line
downloads YouTube videos
can run convert_video_to_audio.py afterwards 
"""



url = input('Please enter a YouTube address:')
valid = validators.url(url)
verify = requests.get(url)

if valid == True and verify.status_code < 400:
  print('Just a moment please')
  try:
    pytube.YouTube(url).streams.get_highest_resolution().download()
    print('Download is complete')
  except:
    print("An exception occurred, probably badly formed URL")
elif valid == True and verify.status_code >= 400:
  print('Not a valid URL')
else:
  print('wanted an else...')
  



### to try it type:
### python my_downloader.py
### and give it a valid YouTube address

""" can try the following examples """
""" https://www.youtube.com/watch?v=Tf-XPGneZEw """
"""https://www.pipsnacks.com/404"""
