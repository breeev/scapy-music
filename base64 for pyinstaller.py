from base64 import b64decode,b64encode
import sounddevice as sd
import soundfile as sf
from scapy.all import sniff
from copy import deepcopy
import numpy as np
from time import time
from tkinter.filedialog import asksaveasfile
your_code = b64encode(b"""
N=100 # number of packets to catch
T=0.1 # duration of beeps
pitch_height_factor=7 # the pitch of beeps will be multiplied by this factor to cover a larger spectrum
pitch_height_offset=100 # the pitch of beeps will be summed with this value to be audible
decrease_speed_factor=1 # the real-time catch of packets will be slowed down to hear them well
fs = 44100 # sample rate used to generate, play and write audio
play=True # set to True to play the output audio
write_to_file=True # set to True to write your file with the end of the script
t=np.arange(0,T,1/fs)
audio=np.arange(0,1,1/fs)
temp=0
def beep(x):
    global audio,temp
    data=deepcopy(t)
    if 'IP' in x:
        print('{:<15} {:<20}'.format(x['IP'].src,str(x.time)))
        for n in x['IP'].src.split('.'):
            data=data+np.sin(2*np.pi*(int(n)*pitch_height_factor+pitch_height_offset)*t)
        if temp and x.time-temp:
            total=np.arange(0,(x.time-temp)*decrease_speed_factor,1/fs)
            if len(data)<len(total):total[-len(data):]=data
        else:total=data
        temp=x.time
        audio=np.append(audio,deepcopy(total))
packets=sniff(prn=lambda x:beep(x),count=N,iface='Wi-Fi')
sd.play(audio, fs)
if not write_to_file:sd.wait()

if write_to_file:
    files = [('Waveform Audio Files', '*.wav'), 
            ('Audio Interchange File Format', '*.aiff,*.aifc'),
            ('Free Lossless Audio Codec', '*.flac')]
    filename=asksaveasfile(filetypes = files, defaultextension = files)
    if filename:sf.write(filename.name,audio,fs)
""")
exec(b64decode(your_code))