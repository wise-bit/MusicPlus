
import urllib.request
import sys
import urllib.parse, re, json
import urllib
import pprint
import youtube_dl
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"; from pygame import mixer
import time
import mutagen.mp3

import quoteGenerator

# os.system("ECHO off")

# Global Variables
videoName = ""
currentIndex = 1
playingIndex = 1

path = ""

# Video information
def video_info(VideoID):

	global videoName

	params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
	url = "https://www.youtube.com/oembed"
	query = urllib.parse.urlencode(params)
	url = url + "?" + query
	response_text = urllib.request.urlopen(url).read()
	data = json.loads(response_text.decode()) 

	# pprint.pprint(data)
	# print(data['title'])

	videoName = data['title']


# fetch link of query string
def link_grabber(query):
	query_string = urllib.parse.urlencode({"search_query" : query + " audio"})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	link = "http://www.youtube.com/watch?v=" + search_results[0]
	video_info(search_results[0])
	download(search_results[0])


# get image

# implement keyboard listening

# Download audio
def download(ID):

	next_index()
	global currentIndex

	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3'
	    }],
	    'prefer_ffmpeg': True,
	    'keepvideo': False,
	    'outtmpl': 'storage/{}.%(ext)s'.format(currentIndex),
	}

	sys.stdout = open(os.devnull, "w")

	abswith youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['http://www.youtube.com/watch?v=' + ID])

	sys.stdout = sys.__stdout__


# Download next one

# Play the thing
def play():

	update_path()

	mp3 = mutagen.mp3.MP3(path)
	mixer.init(frequency=mp3.info.sample_rate)

	print_video_name()

	mixer.music.load(path)
	mixer.music.play()

	next()

	mixer.quit()

def next():

print("Enter 's' to stop music, 't' to set timer, or 'n' to enter new name of song")
after = input("> ")

if after == "s":
	mixer.music.stop()
	print(quoteGenerator.getQuote())

elif after == "t":
	None

elif after == "n":
	next_index()
	link_grabber(query())
	play()

elif after == "f": #finish the current one
	while mixer.music.get_busy() == True:
		continue

elif after == 

else:
	print("invalid option, please try again")
	next()



# Delete old music once it is done

# Store them with appropriate names

# skip and stuff

def print_video_name():
	print("\nNow playing - %s" % videoName)

def update_path():
	global path
	path = '{}/storage/{}.mp3'.format(os.getcwd(), currentIndex)

def query():
	s = input(">> ")
	return s

def next_index():
	global currentIndex
	if currentIndex < 9:
		currentIndex += 1
	else:
		currentIndex = 1

def currently_playing_index():
	global playingIndex
	if playingIndex < 9:
		playingIndex += 1
	else:
		playingIndex = 1
