import pytube

"""
my_downloader.py 03-30-2022
runs at the command line
downloads YouTube videos
"""

url = input('Please enter a YouTube address:')

pytube.YouTube(url).streams.get_highest_resolution().download()
print('Download is complete')

### to try it type:
### python my_downloader.py
### and give it a valid YouTube address

""" 
You can try the following example 
https://www.youtube.com/watch?v=LStXdttFj_o
"""

