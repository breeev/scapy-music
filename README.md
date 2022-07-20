# Scapy Music <img src='https://raw.githubusercontent.com/breeev/scapy-music/main/logo.ico?sanitize=true&raw=true'/>
> Non-random music is cool!  

  While creativity is a big part of music creation, a creation following a set of rules is often more appealing. While creativity may seem random, it's in fact often a very original set of rules that make sense together and that way pleases our senses.  
Why all that gibberish you ask?  

This repo contains <b>a scappy analyzer that plays sounds depending on the network packets in circulation</b>. That means it's supposed to vary depending on the time and place where it's being executed, and will always have a meaning because every communication has one.  
<b>Now working in real time!</b>  

Please note that this script only works with IPv4 adresses.  

# Dependencies  
You will need Scapy, Pygame and Numpy ; the Wheel module may prevent errors. You can use Python pip:
```
pip install wheel
pip install scapy
pip install pygame
pip install numpy
```
You will also need a libcap provider. On Windows there is <a href='https://nmap.org/npcap/'>Nmap</a>, but if you installed <a href='https://www.wireshark.org/download.html'>Wireshark</a> you probably already have it.

# Features
Get ready to hear computers talk to each other!  
This script uses <a href="https://scapy.net/">Scappy</a> to capture packets. If they got a source IP address, then <a href="https://numpy.org/">Numpy</a> is used to set for each address a mix of four sine waves whose pitch are from the four address bytes (slightly offset and multiplied for hearability and diversity).  

While "`no time.py`" has no time support, it plays a track composed of every address found in order. The rhythm comes from the time support introduced in "`main.py`". A realtime version has then been created using pygame (see "`realtime.py`"). And then a loopback version was created. It's even more simple and can sniff packets coming from your own computer for... Your own computer. Loopback packets are here to make components inside your computer talk to each other. It's the most interesting one and really cool to use with Sonic Pi.  
These last files also have <b>settings</b> with comments, you should mess up with them and see what you come up with.  
Finally, "`ScapyRGB`" has nothing to do with sound. It's a keyboard RGB representation of your network activity (takes the first three IP bytes as RGB values) that splits your keyboard in two showing download and upload packets. Beautiful! It uses OpenRGB so be sure to install it along with a client named `openrgb-python` you can install using `pip`.  

You can find old Windows executables in the <a href="https://github.com/breeev/scapy-music/releases">releases</a> section.



This project was made for my father's birthday.
