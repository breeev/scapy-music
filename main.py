from copy import deepcopy
from scapy.all import sniff
import numpy as np
import sounddevice as sd

N=100
fs = 44100
note=440
T=0.1
t=np.arange(0,T,1/fs)
audio=np.arange(0,T*N,1/fs)
def beep(x):
    global audio
    data=deepcopy(t)
    if 'IP' in x:
        print(x['IP'].src)
        for n in x['IP'].src.split('.'):
            data=data+np.sin(2*np.pi*(int(n)*20)*t)
        audio=np.append(audio, deepcopy(data))
#def beep(x):
#    #Beep(x['IP'].src)
#    if 'IP' in x:
#        print(x['IP'].src)
packets=sniff(prn=lambda x:beep(x),count=N,iface='Wi-Fi')
sd.play(audio, fs)
sd.wait(N*T)