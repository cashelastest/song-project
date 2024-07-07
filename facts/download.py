from pytube import YouTube
 
link = input('link: ')
yt = YouTube(link)
yt.streams.first().download()

print("Видео успешно загружено")