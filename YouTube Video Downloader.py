
from pytube import YouTube
def main():
    link = input("Enter youtube video URL?\n ")
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()

main()