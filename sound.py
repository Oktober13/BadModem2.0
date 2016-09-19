#!/usr/bin/python
# import math
# import pyaudio
from scipy import signal
import pyaudio
import math
import time

sentence = "go fish"

def soundaudio(soundlength):

	if soundlength == 0:
		time.sleep(1)
		return

	bitrate = 16000

	freq = 700.0 #Hz
	length = soundlength * 0.25

	numframes = int(bitrate * length)
	restframes = numframes % bitrate
	wavedata = ''

	for x in xrange(numframes):
		wavedata = wavedata+chr(int(math.sin(x/((bitrate/freq)/math.pi))*127+128))

	for x in xrange(restframes):
		wavedata = wavedata+chr(128)

	p = pyaudio.PyAudio()

	stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = bitrate, output = True)
	stream.write(wavedata)
	stream.stop_stream()
	stream.close()
	p.terminate()

	# signal.chirp(1,261.63,5,500.00,method='linear')

def txt2morse(txt):
	txt2mrs = {"a" : "0013", "b" : "3111", "c" : "3131", "d" : "0311", "e" : "0001", "f" : "1131", "g" : "0331", "h" : "1111", "i" : "0011", "j" : "1333", "k" : "0313", "l" : "1311", "m" : "0033", "n" : "0031", "o" : "0333", "p" : "1331", "q" : "3313", "r" : "0131", "s" : "0111", "t" : "0003", "u" : "0113", "v" : "1113", "w" : "0133", "x" : "3113", "y" : "3133", "z" : "3311", " " : "0000", "." : "1111"}

	characters = list(txt)
	morsebits = []

	for letter in characters:
		morsebits.append(txt2mrs[letter])
		morsebits.append("0000")

	# print morsebits
	return morsebits

def mrs2sound()
	morse = txt2morse(sentence)
	# print morse

	for letter in morse:
		for sound in letter:
			sound = int(sound)
			soundaudio(sound)