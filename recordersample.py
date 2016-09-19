from multiprocessing import Process, Queue
import time
import json
import requests
import pyaudio
import wave
import evdev

keystrokes = Queue()
device = evdev.InputDevice('/dev/input/event4')

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

    #stop Recording
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

    record()

    keys = device.active_keys()
    if keys:
        for key in keys:
            if key == 1:  # ESC
                keyqueue.put("esc")
            elif key == 57:  # Space bar
                record()
                filepath = 'recording.wav'  # path to file
                audio = open(filepath,'rb').read()

