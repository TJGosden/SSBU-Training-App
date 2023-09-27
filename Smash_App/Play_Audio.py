import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import playmedia as pm
import sounddevice as sd
import soundfile as sf
import numpy as np

#Cable Output VB-Audio
sd.default.device = "CABLE Input (VB-Audio Virtual C, MME"

def play_audio(targetFileName, gameName):
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    targetFilePath = os.path.join(scriptDirectory, 'Audio/' + gameName + targetFileName)
    audio = pm.File(targetFilePath)
    audio.start()

def play_audio_sd(targetFileName, gameName):
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    targetFilePath = os.path.join(scriptDirectory, 'Audio/' + gameName + targetFileName)
    data, fs = sf.read(targetFilePath)
    sd.play(data, fs)
    #sd.wait()
