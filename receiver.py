from scipy import signal
import math
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave
import sys
from multiprocessing import Process, Queue
import time
import json
import requests
import wave
import evdev

def lowPass(filterorder, sig):

	#function takes in an array that represents a signal and returns a version that has been through a low pass filter

	b, a = signal.butter(filterorder, .05) #create butterworth filter which exports parameters for filtfilt, given order and cutoff
	v = signal.filtfilt(b, a, sig)
	return v

def movingAverage (values, window):
	weights = np.repeat(1.0, window)/window
	sma = np.convolve(values, weights, 'valid')
	return sma

def letters(wave):
	amp_threshold = 7 #this is a placeholder
	dash_threshold = 1000 #distinction between dot and dash
	new_threshold = 3000 #threshold to be a new letter
	chunks = isplit(wave, amp_threshold)
	letterlist = []
	for chunk in chunks:
		if chunk[0] > amp_threshold: #dot or dash
			if len(chunk) > dash_threshold:
				letterlist.append(3)
			else:
				letterlist.append(1)
		else: #long pause or short pause
			if len(chunk) > new_threshold:
				letterlist.append(0)



 def isplit(iterable,splitters):
 	#a very nice split function, splits the iterable(list) on the splitter value
    return [list(g) for k,g in itertools.groupby(iterable,lambda x:x in splitters) if not k]


def record():
	""" Records audio while the space bar is pressed and saves the audio to
	recording.wav. """
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	WAVE_OUTPUT_FILENAME = "recording.wav"

	audio = pyaudio.PyAudio()
	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
						rate=RATE, input=True,
						frames_per_buffer=CHUNK)
	frames = []

	while 57 in device.active_keys():
		data = stream.read(CHUNK)
		frames.append(data)
	print "finished recording"

	stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

if __name__ == '__main__':

	keystrokes = Queue()
	device = evdev.InputDevice('/dev/input/event4')

	keys = device.active_keys()
	if keys:
		for key in keys:
			if key == 1:  # ESC
				keyqueue.put("esc")
			elif key == 57:  # Space bar
				record()
				filepath = 'recording.wav'  # path to file
				audio = open(filepath,'rb').read()

	#sample chirp for the low pass filter function
	Fs = 8000 #sample rate
	f = 10 #number of waves
	sample = 8000
	x = np.arange(sample)
	y = np.sin(2 * np.pi * f * x / Fs) 

	t = np.linspace(0, 10, 5001)
	w = signal.chirp(t, f0=12.5, f1=2.5, t1=10, method='linear')

	lowpassed = lowPass(audio)
	smooth_magnitude = movingAverage(abs(lowpassed), 5) #takes the absolute value, then a moving average of that




