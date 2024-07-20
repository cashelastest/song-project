from pytube import YouTube
 
def download_from_yt(url):

	link = input('link: ')
	yt = YouTube(link)
	yt.streams.first().download()
	print("Видео успешно загружено")