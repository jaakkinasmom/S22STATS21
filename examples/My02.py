# Download a YouTube video
# need to install pytube for this to run
# suggest trying it first in a virtual environment
# will ask for input of a url
# class example was url = 'https://www.youtube.com/watch?v=LStXdttFj_o'

import pytube

pytube.YouTube(url).streams.get_highest_resolution().download()


