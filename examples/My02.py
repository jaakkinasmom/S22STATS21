# Download a YouTube video
# need to install pytube for this to run
# suggest trying it first in a virtual environment
# will ask for input of a url

import pytube

pytube.YouTube(url).streams.get_highest_resolution().download()


