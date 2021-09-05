import os
import eel
from pygame import mixer 
from mutagen.mp3 import MP3
import threading

print('')
print(r'example:- C:\Users\Admin\Desktop\music')
dir = input('ENTER YOUR MUSIC DIRECTORY:- ')
print('')

eel.init("web")		# initialises eel
arr = []	#array keeps track of all songs
i = 0		
o = 0		#counter for songs
status = 1	#for play/pause status
vol = 1.0	#controls volume (1.0 = maximum volume)

# adds all songs to array
mylist = os.listdir(dir)
while i != len(mylist):
    arr.append(mylist[i])
    i += 1		

@eel.expose	
def play():
	# plays music
	global status
	status = 1
	mixer.music.unpause()
	return 'play'

@eel.expose	
# pauses music
def pause():
	global status
	status = 0
	mixer.music.pause()
	return 'pause'

@eel.expose	
# decreases volume
def vol_up():
	global vol
	vol += 0.1
	mixer.music.set_volume(vol)
	return 'vol_up'

@eel.expose
# increases volume
def vol_down():
	global vol
	vol -= 0.1
	mixer.music.set_volume(vol)
	return 'vol_down'

@eel.expose	
def next():
	global arr
	global o
	global status
	# if music is not paused
	if status == 1:	
		if o + 1 != len(arr):
			# loads and plays next song
			try:
				o += 1
				mixer.music.load(dir + "\\" + arr[o])
			except:
				return
			mixer.music.play()
			print(arr[o])
			return [arr[o], 'next']
		# if all songs have been played, it starts playing from the begining
		else:
			o = 0
			mixer.music.load(dir + "\\" + arr[o])
			mixer.music.play()
			print(arr[o])
			return [arr[o], 'next']
	
	# if music is paused
	elif status == 0:
		if o + 1 != len(arr):
			# loads and plays next song
			try:
				o += 1
				mixer.music.load(dir + "\\" + arr[o])
			except:
				o += 1
				mixer.music.load(dir + "\\" + arr[o])
				return
			mixer.music.play()
			mixer.music.pause()
			print(arr[o])
			return [arr[o], 'next']
		# if all songs have been played, it starts playing from the begining
		else:
			o = 0
			mixer.music.load(dir + "\\" + arr[o])
			mixer.music.play()
			print(arr[o])
			return [arr[o], 'next']

@eel.expose	
def previous():
	global arr
	global o
	global status
	# if music is not paused
	if status == 1:
		# loads and plays previous song
		try:
			o -= 1
			mixer.music.load(dir + "\\" + arr[o])
		except:
			return
		mixer.music.play()
		print(arr[o])
		return [arr[o], 'previous']
	# if music is paused
	elif status == 0:
		# loads and plays previous song
		try:
			o -= 1
			mixer.music.load(dir + "\\" + arr[o])
		except:
			return
		mixer.music.play()
		mixer.music.pause()
		print(arr[o])
		return [arr[o], 'previous']

@eel.expose
def main():
	global arr
	global o
	global status

	# updates the HTML header with the current playing song
	eel.name_update(arr[o])
	print(arr[o])

	# gets song length
	def length():
		length = MP3(dir + "\\" + arr[o]).info.length
		return int(length)
	
	# updates song slider bar
	while mixer.music.get_busy() != 0:
		eel.time(int((((mixer.music.get_pos()) / 1000) / length()) * 100))
		while status == 0:
			o
			eel.time(int((((mixer.music.get_pos()) / 1000) / length()) * 100))
	
	# plays next song if song has finished
	if mixer.music.get_busy() == 0:
		o += 1
		if o != len(arr):
			mixer.music.load(dir + "\\" + arr[o])
			mixer.music.play()
			main()
		else:
			o = 0
			mixer.music.load(dir + "\\" + arr[o])
			mixer.music.play()
			main()

# Starts the index.html file
def start():
	eel.start("index.html")

mixer.init()
mixer.music.load(dir + '\\' + arr[o])
mixer.music.play()

if __name__ == '__main__':
	threading.Thread(target = start).start()
	main()