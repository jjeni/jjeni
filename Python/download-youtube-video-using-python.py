from pytube import YouTube
url = 'Video URL'
path = 'path/dowbload' #download path
my_video = YouTube(url)
my_video = my_vide.streams.first() #get higher resolution video
my_video.download(path)
