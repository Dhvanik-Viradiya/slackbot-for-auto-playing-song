# url mapping only
# This bot will work only in public channel


import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from threading import Thread
import time
import vlc
import pafy
from youtubesearchpython import VideosSearch


env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

# @app.route('/')
def home():
	print("opop")
	t = Thread(target=loadVideo)
	t.start()
	t.join()


slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel="#jambox-testing",text="Hi, I am jambox bot. Now you can use commands (pinned msg) to control me :)")

Instance = vlc.Instance()
player = Instance.media_player_new()

video_link = []
num = 0
resume = True
next_song = False
volume = 80
print("radhe radhe")
@slack_event_adapter.on('message')
def message(payload):
	print("message")
	global video_link
	global num
	global Instance
	global player
	global resume
	global next_song
	global volume
	if not num:
		num+=1
		home()
	event = payload.get('event', {})
	channel_id = event.get('channel')
	user_id = event.get('user')
	text = event.get('text')
	if text==";pause":
		resume = False
		player.pause()
	elif text==";resume":
		resume = True
		player.play()
	elif text==";next":
		next_song = True
	elif text==";sound++":
		volume+=15
		volume = min(99,volume)
		print("volume is pressed")
		x=player.audio_set_volume(volume)
		print(text, x, volume)
	elif text==";sound--":
		volume-=15
		volume = max(volume,1)
		player.audio_set_volume(volume)
	elif text and text.startswith(";play "):
		text = text.lstrip(";play ").strip()
		videosSearch = VideosSearch(text, limit = 1)
		result = videosSearch.result()
		text = result["result"][0]["link"]
		if text not in video_link:
			video_link.append(text)
	elif isinstance(text,str):
		text = text.lstrip("<").rstrip(">")
		if text not in video_link:
			video_link.append(text)
	print(text)



def loadVideo():
	# pass
	global video_link
	global Instance
	global player
	global resume
	global next_song
	global client
	while True:
		print("radhe")
		if (not resume or player.is_playing()) and not next_song:
			print("inside resume")
			time.sleep(5)
			continue
		elif next_song:
			print("inside next")
			next_song = False
		try:
			if len(video_link):
				url = video_link[0]
				print(url)
				try:
					video = pafy.new(url)
					best = video.getbestaudio()
					playurl = best.url
					media = Instance.media_new(playurl)
					media.get_mrl()
					player.set_media(media)
					print("radhe")
					player.play()
					video_duration = player.get_length()
					print(video_duration)
					print(video.length)
					print("shyam")
					video_link.remove(url)
					time.sleep(10)
				except Exception as e:
					print(e)
					video_link.remove(url)
					next_song = True
					time.sleep(1)
			else:
				time.sleep(5)
		except KeyboardInterrupt:
			client.chat_postMessage(channel="#jambox-testing",text="I hope you enjoyed. Bye Bye!")
			print('KeyboardInterrupt exception is caught')
			break

if __name__ == "__main__":
	app.run(debug=True)
	