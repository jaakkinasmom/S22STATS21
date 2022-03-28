import os
import sys
from moviepy.editor import VideoFileClip

def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Video to audio converter uses the MoviePy library
    which uses `ffmpeg` (must be installed)"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")


if __name__ == "__main__":
    vf = sys.argv[1]
    convert_video_to_audio_moviepy(vf)

""" Use example
$ python convert_video_to_audio.py my_video.mp4
"""
