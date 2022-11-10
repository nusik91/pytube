import youtube_dl

ydl_opts = {}

def download():
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([vid])

loading = 1
while (loading == int(1)):
	link_of_the_video = input("вставьте URL для скачивания видео:- ")
	vid = link_of_the_video.strip()

	download()
	loading = int(input("Введите 1 чтобы скачать ещё видео \n или 0 если закончили "))
