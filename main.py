from progressbar import Timer,Bar,ETA,ProgressBar
widgets = ['Importing libs: ',
           Bar('O'),' (',
           ETA(), ') ',
]
bar=ProgressBar(maxval=6,widgets=widgets).start()
from copy import deepcopy
bar.update(1)
from scapy.all import sniff
bar.update(2)
from numpy import arange,sin,pi,append as app
bar.update(3)
from sounddevice import play as pl,wait
bar.update(4)
from soundfile import write
bar.update(5)
from tkinter.filedialog import asksaveasfile
bar.update(6)

##SETTINGS
N=100 # number of packets to catch
T=0.1 # duration of beeps
pitch_height_factor=7 # the pitch of beeps will be multiplied by this factor to cover a larger spectrum
pitch_height_offset=100 # the pitch of beeps will be summed with this value to be audible
decrease_speed_factor=1 # the real-time catch of packets will be slowed down to hear them well
fs = 44100 # sample rate used to generate, play and write audio
play=True # set to True to play the output audio
write_to_file=True # set to True to write your file with the end of the script

t=arange(0,T,1/fs)
audio=arange(0,1,1/fs)
temp=0
a=0
def beep(x):
    global audio,temp,a
    a+=1
    data=deepcopy(t)
    bar.update(a)
    if 'IP' in x:
        #print(x['IP'].src)
        for n in x['IP'].src.split('.'):
            data=data+sin(2*pi*(int(n)*pitch_height_factor+pitch_height_offset)*t)
        if temp and x.time-temp:
            total=arange(0,(x.time-temp)*decrease_speed_factor,1/fs)
            if len(data)<len(total):total[-len(data):]=data
        else:total=data
        temp=x.time
        audio=app(audio,deepcopy(total))

widgets = ['Catching packets: ',
           Bar('♩'),' (',
           ETA(), ') ',
]
bar=ProgressBar(maxval=N,widgets=widgets).start()

try:packets=sniff(prn=lambda x:beep(x),count=N,iface=input('Enter your target interface name (for Windows see the name given by ipconfig):'))
except OSError:print('Wrong interface name')
pl(audio, fs)
if not write_to_file:wait()

if write_to_file:
    files = [('Waveform Audio Files', '*.wav'), 
            ('Audio Interchange File Format', '*.aiff,*.aifc'),
            ('Free Lossless Audio Codec', '*.flac')]
    filename=asksaveasfile(filetypes = files, defaultextension = files)
    if filename:write(filename.name,audio,fs)