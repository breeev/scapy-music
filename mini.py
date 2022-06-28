P=int
D=print
from os import system as A
A('COLOR 0C')
D('\n .d8888b.                    888                        \nd88P  Y88b                   888                        \nY88b.                        888                        \n "Y888b.    .d8888b  8888b.  88888b.  888  888 88888b.  \n    "Y88b. d88P"        "88b 888 "88b 888  888 888 "88b \n      "888 888      .d888888 888  888 888  888 888  888 \nY88b  d88P Y88b.    888  888 888 d88P Y88b 888 888 d88P \n "Y8888P"   "Y8888P "Y888888 88888P"   "Y88888 88888P"  \n                                           888 888      \n                                      Y8b d88P 888      \n                                       "Y88P"  888      ')
D('⛹️\u200d♂️ importing libs...')
from scapy.all import sniff,get_if_addr as E,conf
from numpy import sin,pi,linspace as F,float32 as G
from contextlib import redirect_stdout as H
with H(None):from pygame.mixer import init,Sound
B=0.1
I=7
J=100
C=44100
K=True
L=0.1
M=F(0,B*2*pi,P(B*C))
init(frequency=C,size=32)
def N(hz):A=L*sin(hz*M).astype(G);B=Sound(A);B.play(0)
def O(x):
	for A in x['IP'].src.split('.'):N(P(A)*I+J)
D('\x1b[1A\x1b[2K✅ ready.')
A('COLOR 0A')
sniff(prn=lambda x:O(x),filter='ip'+K*(' and not (ip src '+E(conf.iface)+')'),store=0)