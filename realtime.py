from scapy.all import sniff
from numpy import sin,pi,linspace,float32
from pygame.mixer import init,Sound

##SETTINGS
T=0.2 # duration of beeps
pitch_height_factor=7 # the pitch of beeps will be multiplied by this factor to cover a larger spectrum
pitch_height_offset=100 # the pitch of beeps will be summed with this value to be audible
fs = 44100 # sample rate used to generate, play and write audio

x=linspace(0, T * 2 * pi, int(T * fs))
init(size=32)
def play(hz):
    buffer = sin(hz*x).astype(float32)
    sound = Sound(buffer)
    sound.play(0)

def beep(x):
    if 'IP' in x:
        for n in x['IP'].src.split('.'):play(int(n)*pitch_height_factor+pitch_height_offset)

sniff(prn=lambda x:beep(x))